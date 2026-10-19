"""R1: exact two-case, two-slot public-state model. Standard library only.
Closed form, decentralized equilibrium, posted opportunity-loss toll, and
independent exhaustive schedule enumeration over a latent-state outcome table.
All values synthetic. Transfers are excluded from total firm payoff.
"""
from dataclasses import dataclass, asdict, replace
from itertools import product
from pathlib import Path
import csv,json,math
OUT=Path(__file__).resolve().parents[1]/'results';OUT.mkdir(exist_ok=True)
@dataclass(frozen=True)
class Case:
 p:float=.5
 S:float=100
 r:float=0
 q:float=.7
 c:float=1
 d:float=0
 h:float=.02

def primitives(x):
 g=x.S*(1-(1-x.r)*min(x.p,1-x.p))
 # Bayes classification success: sum of maximum joint state/signal probabilities.
 acc=max(x.p*x.q,(1-x.p)*(1-x.q))+max(x.p*(1-x.q),(1-x.p)*x.q)
 M=x.S*(x.r+(1-x.r)*acc)
 s=1-x.h;b=s*M-x.c-x.d-g;ell=x.d+x.h*g
 w=max(0,s*b-ell);u=max(0,b)-w
 return dict(g=g,M=M,b=b,ell=ell,w=w,u=u)

def closed(a,b):
 x,y=primitives(a),primitives(b);G=x['g']+y['g']
 options={'stop':0,'A_first':x['b']+y['w'],'B_first':y['b']+x['w']}
 k=max(options,key=options.get)
 return G+options[k],k,options

def local(a,b,tax=0,deadline=2):
 x,y=primitives(a),primitives(b);G=x['g']+y['g']
 if deadline==0:return G,'stop'
 if x['b']>tax+1e-10:
  later=deadline==2 and (1-b.h)*(y['b']-tax)-y['ell']>1e-10
  return G+x['b']+(y['w'] if later else 0),'A_then_B' if later else 'A_only'
 if y['b']>tax+1e-10:return G+y['b'],'B_only'
 return G,'stop'

def corrective(a,b):
 x,y=primitives(a),primitives(b);G=x['g']+y['g']
 # Posted charge only for A's priority claim now; zero for deferred use.
 toll=y['u']
 if x['b']-toll>x['w']+1e-10:
  return G+x['b']+y['w'],'A_first',toll
 if y['b']>1e-10:return G+y['b']+x['w'],'B_first',toll
 # A may optimally wait when both urgency indices are zero; one slot remains.
 return G+max(0,x['b']),'A_deferred' if x['b']>0 else 'stop',toll

def root_actions():
 for mask in range(4):
  yield mask,None
  for i in range(2):
   if mask>>i&1:yield mask,i

def raw_scenarios(a,b):
 xs=(a,b)
 for th in product(range(2),repeat=2):
  for ys in product(range(2),repeat=2):
   base=1.
   for i,x in enumerate(xs):
    base*= (x.p if th[i] else 1-x.p)*(x.q if ys[i]==th[i] else 1-x.q)
   for alive in product(range(2),repeat=4):
    prob=base
    for i,x in enumerate(xs):
     for t in range(2):prob*=1-x.h if alive[2*i+t] else x.h
    if prob>0:yield prob,th,ys,alive

def act(x,theta,y=None):
 if y is None:choice=int(x.p>=.5)
 else:
  z1=x.p*(x.q if y else 1-x.q)
  z0=(1-x.p)*((1-x.q) if y else x.q)
  choice=int(z1>=z0)
 return x.S if choice==theta else x.r*x.S

def independent_enumeration(a,b):
 # No b/w/u formulas in this evaluator. Enumerates root action, all last-slot
 # contingent scheduling maps, latent states, signals and all hazard coins.
 xs=(a,b);scenarios=list(raw_scenarios(a,b));best=-math.inf;records=[];count=0
 for mask,selected in root_actions():
  observations={}
  for prob,th,ys,alive in scenarios:
   remaining=tuple(i for i in range(2) if mask>>i&1 and i!=selected and alive[2*i])
   signal='none' if selected is None else ('dead' if not alive[2*selected] else str(ys[selected]))
   key=(remaining,signal);observations[key]=(None,)+remaining
  keys=tuple(observations)
  for choices in product(*(observations[k] for k in keys)):
   mapping=dict(zip(keys,choices));total=0.
   for prob,th,ys,alive in scenarios:
    reward=0.
    for i,x in enumerate(xs):
     if not(mask>>i&1):reward+=act(x,th[i])
     else:
      reward-=x.d
      if selected==i:
       reward-=x.c
       if alive[2*i]:reward+=act(x,th[i],ys[i])
    remaining=tuple(i for i in range(2) if mask>>i&1 and i!=selected and alive[2*i])
    signal='none' if selected is None else ('dead' if not alive[2*selected] else str(ys[selected]))
    last=mapping[(remaining,signal)]
    for i in remaining:
     x=xs[i]
     if last==i:
      reward-=x.c+x.d
      if alive[2*i+1]:reward+=act(x,th[i],ys[i])
     else:reward+=act(x,th[i])
    total+=prob*reward
   count+=1
   records.append({'root_retained_mask':mask,'root_selected':selected,'last_slot_map':str(mapping),'payoff':total})
   best=max(best,total)
 return best,count,records

A=Case();B=Case(q=.9,h=.2)
scenarios=[('congestion',A,B),('belief_low_urgency',A,replace(B,p=.705)),('reversal_low_r',A,Case(h=.022)),('reversal_high_r',replace(A,r=.5),Case(h=.022)),('separable_no_holding',replace(A,h=0),replace(B,h=0)),('only_B_worth_research',replace(A,c=30),B)]
rows=[];checks=0;allrecords=[]
for name,a,b in scenarios:
 v,order,opts=closed(a,b);ve,n,recs=independent_enumeration(a,b)
 assert abs(v-ve)<1e-8;checks+=1
 vc,oc,toll=corrective(a,b);assert abs(vc-v)<1e-8;checks+=1
 for r in recs:r['scenario']=name
 allrecords+=recs
 rows.append(dict(scenario=name,**{'A_'+k:v for k,v in primitives(a).items()},**{'B_'+k:v for k,v in primitives(b).items()},optimal=v,optimal_order=order,local=local(a,b)[0],deadline0=local(a,b,deadline=0)[0],deadline1=local(a,b,deadline=1)[0],posted_rule=vc,posted_toll=toll,enumerated_policies=n))
# Deterministic parameter grid plus a prespecified subset with full enumeration.
for p,S,r,q,h,c in product([.35,.5],[40,100],[0,.5],[.6,.85],[0,.08,.25],[1,7]):
 a=Case(p=p,S=S,r=r,q=q,h=h,c=c,d=1)
 b=Case(p=1-p,S=120,r=.2,q=.75,h=.06,c=2,d=0)
 v=closed(a,b)[0]
 assert abs(corrective(a,b)[0]-v)<1e-8;checks+=1
 assert v+1e-8>=local(a,b)[0];checks+=1
 # Never use transfers as welfare expense; tax values only alter private choices.
 if checks%16 in [0,1]:
  ve,n,_=independent_enumeration(a,b);assert abs(v-ve)<1e-7;checks+=1
# Explicit full enumeration on 36 additional cases, selected without fitting results.
for p,q,h in product([.2,.5,.8],[.6,.8],[0,.05,.2]):
 a=Case(p=p,q=q,h=h,d=.5);b=Case(p=.4,S=70,r=.4,q=.85,h=.1,c=2)
 assert abs(independent_enumeration(a,b)[0]-closed(a,b)[0])<1e-7;checks+=1
# Strict inequalities in the common-charge impossibility example.
x,y=primitives(A),primitives(B)
assert y['u']>x['u']>0 and x['w']>0 and y['w']>0;checks+=1
assert abs(closed(A,B)[0]-137.248)<1e-9;checks+=1
for tax in [0,1,5,10,17.59,17.6,18,20,21,30]:
 assert local(A,B,tax)[0]<closed(A,B)[0]-1e-8;checks+=1
# Closed-form reversal derivatives verified with a finite change within retain regime.
a0=primitives(A);a1=primitives(replace(A,r=.5));b=primitives(Case(h=.022))
assert a0['b']>a1['b'] and a0['u']<b['u']<a1['u'];checks+=1
# Tight equality / zero urgency positive implementation boundary.
for h in [0,.02]:
 a=replace(A,h=h);b=replace(B,h=0)
 assert abs(corrective(a,b)[0]-closed(a,b)[0])<1e-8;checks+=1
with (OUT/'joint_results.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
with (OUT/'joint_enumerated_policies.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(allrecords[0]));w.writeheader();w.writerows(allrecords)
(OUT/'joint_parameters.json').write_text(json.dumps({name:{'A':asdict(a),'B':asdict(b)} for name,a,b in scenarios},indent=2))
summary={'synthetic':True,'checks_passed':checks,'method':'closed-form optimum compared with independent exhaustive two-slot policy and latent-outcome enumeration','scope':'two cases; one binary experiment each; independent states; two slots; instant terminal action; independent expiration; nonnegative holding costs','named_scenarios':len(rows),'named_policy_rows':len(allrecords),'enumeration_includes':'idle slots, immediate retirement of any subset, signal-contingent last-slot choices, all positive-probability hazard and latent-state paths','no_seed_needed':True}
(OUT/'joint_validation.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
for row in rows:print(row)
