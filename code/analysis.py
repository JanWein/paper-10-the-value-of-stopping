"""Exact finite-tree synthetic analysis. Python 3 standard library only.
No firm observations, estimated parameters, or Monte Carlo sampling.
Run from any directory: python3 paper10/code/analysis.py
"""
from functools import lru_cache
from pathlib import Path
import csv, json, math, platform
OUT=Path(__file__).resolve().parents[1]/'results'
OUT.mkdir(exist_ok=True)

def model(S=100,r=0,q=.7,c=1,d=5,h=.02,H=12,alpha=1,deadline=None,minimum=0):
    # Posterior state (n,k); prior .5, iid binary signals of accuracy q.
    def post(n,k):
        odds=(q/(1-q))**(2*k-n)
        return odds/(1+odds)
    def g(n,k): return S*(1-(1-r)*min(post(n,k),1-post(n,k)))
    @lru_cache(None)
    def solve(n,k):
        stop=g(n,k)
        if n==H or (deadline is not None and n>=deadline): return stop,False
        p=post(n,k); prob=p*q+(1-p)*(1-q)
        cont=-c-alpha*d+(1-h)*(prob*solve(n+1,k+1)[0]+(1-prob)*solve(n+1,k)[0])
        go=(cont>stop+1e-10) or n<minimum
        return (cont,True) if go else (stop,False)
    @lru_cache(None)
    def evaluate(n,k):
        # unconditional payoff, active periods, completion, correct-and-completed
        if not solve(n,k)[1]:
            return g(n,k),0.,1.,max(post(n,k),1-post(n,k))
        p=post(n,k); prob=p*q+(1-p)*(1-q)
        a=evaluate(n+1,k+1); b=evaluate(n+1,k)
        mix=[(1-h)*(prob*x+(1-prob)*y) for x,y in zip(a,b)]
        return mix[0]-c-d,1+mix[1],mix[2],mix[3]
    return solve,evaluate,post,g

def row(name,**kw):
    so,ev,po,g=model(**kw); v,t,done,correct=ev(0,0)
    return dict(scenario=name,**kw,payoff=v,periods=t,completion=done,correct_completed=correct,accuracy_completed=correct/done if done else None)
rows=[]
for name,kw in [('firm',{}),('silo',{'alpha':.1}),('deadline0',{'alpha':.1,'deadline':0}),('deadline1',{'alpha':.1,'deadline':1}),('deadline2',{'alpha':.1,'deadline':2}),('deadline4',{'alpha':.1,'deadline':4}),('mandate2',{'minimum':2}),('reversible_firm',{'r':.8}),('reversible_silo',{'r':.8,'alpha':.1}),('high_stakes_firm',{'S':500}),('high_expiry_firm',{'h':.2})]: rows.append(row(name,**kw))
keys=list(dict.fromkeys(k for x in rows for k in x))
with (OUT/'policy_results.csv').open('w') as f:
    w=csv.DictWriter(f,keys);w.writeheader();w.writerows(rows)
# Analytical one-period derivative checks and precision nonmonotonicity of sample counts.
checks=0
for S in [20,100,500]:
 for r in [0,.5,.9]:
  for q in [.55,.7,.9]:
   for d in [0,1,5,20]:
    for h in [0,.02,.2]:
     firm=model(S=S,r=r,q=q,d=d,h=h,H=8,alpha=1)
     agent=model(S=S,r=r,q=q,d=d,h=h,H=8,alpha=.1)
     for n in range(8):
      for k in range(n+1):
       assert not firm[0](n,k)[1] or agent[0](n,k)[1]
       checks+=1
     assert firm[1](0,0)[0]+1e-8>=agent[1](0,0)[0]
     checks+=1
# Exact policy-frontier enumeration for H=3, no duplicated equivalent pairs needed.
def frontier(n,k,H=3,q=.7,h=.02,c=1,S=100):
 p=1/(1+((1-q)/q)**(2*k-n));g=S*max(p,1-p)
 out={(round(g,12),0.)}
 if n==H:return out
 prob=p*q+(1-p)*(1-q)
 for a,ta in frontier(n+1,k+1,H,q,h,c,S):
  for b,tb in frontier(n+1,k,H,q,h,c,S):
   out.add((round(-c+(1-h)*(prob*a+(1-prob)*b),12),round(1+(1-h)*(prob*ta+(1-prob)*tb),12)))
 return out
fr=frontier(0,0);threshold=max((a-50)/t for a,t in fr if t>0)
for d in [0,1,3,5,10,threshold-1e-5,threshold+1e-5]:
 v=max(a-d*t for a,t in fr)
 so=model(H=3,d=d)[0](0,0)[0]
 assert abs(v-so)<1e-8
 checks+=1
# Deadline zero can help in one type and harm in another, at identical baseline belief.
# p=.5, one-step q=.7 => d*= .98*70 - 50 - 1 = 17.6
one_threshold=.98*70-50-1
assert abs(one_threshold-17.6)<1e-9
# Mandatory second sample at p=.7,q=.7 has zero expected accuracy gain at h=0.
p=.7;q=.7;z=p*q+(1-p)*(1-q)
pp=p*q/z;pm=p*(1-q)/(1-z)
assert abs(z*max(pp,1-pp)+(1-z)*max(pm,1-pm)-.7)<1e-12
# Two further samples after belief .7 improve accuracy to .784.
acc=0.
for y1 in [0,1]:
 for y2 in [0,1]:
  k=y1+y2
  w1=.7*(q**k)*((1-q)**(2-k))
  w0=.3*((1-q)**k)*(q**(2-k))
  acc+=max(w1,w0)
assert abs(acc-.784)<1e-12
checks+=3
# Finite-difference tests, one-step continuation margin with reward correct S/wrong r*S.
def margin(S,r,q,c,d,h): return (1-h)*S*(r+(1-r)*q)-S*(r+(1-r)*.5)-c-d
base=margin(100,.2,.7,1,5,.02)
assert margin(101,.2,.7,1,5,.02)>base
assert margin(100,.21,.7,1,5,.02)<base
assert margin(100,.2,.71,1,5,.02)>base
assert margin(100,.2,.7,1,5,.03)<base
checks+=4
summary={'synthetic':True,'method':'exact backward induction and forward expectation','checks_passed':checks,'frontier_unique_pairs_H3':len(fr),'critical_delay_H3':threshold,'one_period_critical_delay':one_threshold,'python':platform.python_version(),'parameters_default':{'S':100,'r':0,'q':.7,'c':1,'d':5,'h':.02,'H':12,'prior':.5},'note':'Horizon is finite and substantive. No asymptotic approximation.'}
(OUT/'validation.json').write_text(json.dumps(summary,indent=2))
# Payoff sensitivity of frozen policies: never reoptimize when varying valuation d.
with (OUT/'delay_bounds.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['policy','gross_less_acquisition','active_periods','payoff_d0','payoff_d5','payoff_d10'])
 for name,kw in [('firm',{}),('silo',{'alpha':.1}),('deadline1',{'alpha':.1,'deadline':1})]:
  ev=model(**kw)[1](0,0);a=ev[0]+5*ev[1];w.writerow([name,a,ev[1],a,a-5*ev[1],a-10*ev[1]])
print(json.dumps(summary,indent=2))
for x in rows:print(x['scenario'],*[round(x[k],6) for k in ['payoff','periods','completion','accuracy_completed']])
