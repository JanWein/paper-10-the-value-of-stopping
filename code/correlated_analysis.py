"""R2: two cases, two slots, one experiment each, correlated binary states.
Exact Fraction arithmetic for the explicit final-slot formula and root solution.
An independent physical-path enumerator checks the finite joint policy tree.
No random samples, fitted parameters, general queue, or simulation campaign.
"""
from fractions import Fraction as F
from itertools import product
from dataclasses import dataclass,asdict
from functools import lru_cache
from pathlib import Path
import csv,json
OUT=Path(__file__).resolve().parents[1]/'results';OUT.mkdir(exist_ok=True)
TH=((0,0),(0,1),(1,0),(1,1))
def f(x):return F(str(x))
@dataclass(frozen=True)
class Case:
 S:F=F(100)
 r:F=F(0)
 q:F=F(4,5)
 c:F=F(1)
 d:F=F(0)
 h:F=F(0)

def posterior(mu,i,y,cases):
 weights=[v*(cases[i].q if th[i]==y else 1-cases[i].q) for th,v in zip(TH,mu)]
 z=sum(weights)
 return z,tuple(v/z for v in weights) if z else mu

def g(mu,i,cases):
 p=sum(v for th,v in zip(TH,mu) if th[i]);x=cases[i]
 return x.S*(x.r+(1-x.r)*max(p,1-p))

def signal_mean(mu,active,target,cases):
 return sum(z*g(m,target,cases) for y in [0,1] for z,m in [posterior(mu,active,y,cases)])

def last(mu,L,E,cases):
 """Explicit theorem formula; also return case payoff components and plan."""
 G=sum(g(mu,i,cases) for i in L)
 comps0=tuple(g(mu,i,cases) if i in L else F(0) for i in range(2))
 opts=[(G,None,(),comps0)]
 for i in L:
  if i not in E:continue
  xi=cases[i];si=1-xi.h
  bi=si*signal_mean(mu,i,i,cases)-xi.c-xi.d-g(mu,i,cases)
  retained=[i];comps=list(comps0);comps[i]+=bi
  for j in L:
   if j==i:continue
   xj=cases[j];sj=1-xj.h
   cross=sj*si*(signal_mean(mu,i,j,cases)-g(mu,j,cases))-xj.d-xj.h*g(mu,j,cases)
   if cross>0:retained.append(j);comps[j]+=cross
  opts.append((sum(comps),i,tuple(sorted(retained)),tuple(comps)))
 return max(opts,key=lambda x:x[0]),opts

def branches(mu,R,i,cases):
 for bits in product([0,1],repeat=len(R)):
  S=tuple(k for k,b in zip(R,bits) if b)
  z=F(1)
  for k,b in zip(R,bits):z*=1-cases[k].h if b else cases[k].h
  if not z:continue
  if i is not None and i in S:
   for y in [0,1]:
    py,m=posterior(mu,i,y,cases)
    if py:yield z*py,m,S,str(y)
  else:yield z,mu,S,'none'

def solve(mu,cases):
 records=[]
 for mask in range(4):
  R=tuple(i for i in range(2) if mask>>i&1)
  for active in (None,)+R:
   E=tuple(i for i in range(2) if i!=active)
   comps=[g(mu,i,cases) if i not in R else -cases[i].d for i in range(2)]
   if active is not None:comps[active]-=cases[active].c
   detail=[]
   for prob,m,S,y in branches(mu,R,active,cases):
    best,_=last(m,S,E,cases)
    for i in range(2):comps[i]+=prob*best[3][i]
    detail.append({'probability':str(prob),'survivors':str(S),'first_signal':y,'posterior':list(map(str,m)),'last_active':best[1],'last_retained':str(best[2]),'last_value':str(best[0])})
   records.append({'root_mask':mask,'root_active':active,'value':sum(comps),'components':tuple(comps),'branches':detail})
 return max(records,key=lambda x:x['value']),records

# Independent enumeration: no use of g, signal_mean, last or solve in evaluation.
def raw_paths(mu,cases):
 for th,pth in zip(TH,mu):
  for ys in product([0,1],repeat=2):
   z=pth
   for i,x in enumerate(cases):z*=x.q if ys[i]==th[i] else 1-x.q
   for alive in product([0,1],repeat=4):
    pr=z
    for i,x in enumerate(cases):
     for t in range(2):pr*=1-x.h if alive[2*i+t] else x.h
    if pr:yield float(pr),th,ys,alive

def physical_terminal(mu,i,obs,cases,theta):
 weights=[float(v) for v in mu]
 for k,y in obs:
  for n,th in enumerate(TH):weights[n]*=float(cases[k].q if th[k]==y else 1-cases[k].q)
 p1=sum(w for th,w in zip(TH,weights) if th[i]);p0=sum(w for th,w in zip(TH,weights) if not th[i])
 choice=int(p1>=p0)
 return float(cases[i].S if choice==theta[i] else cases[i].r*cases[i].S)

def final_plans(L,E):
 # No final idle need be enumerated: it produces no signal and is dominated
 # by stopping all retained cases at this boundary, under nonnegative costs.
 yield None,()
 for i in L:
  if i in E:
   others=tuple(j for j in L if j!=i)
   for bits in product([0,1],repeat=len(others)):
    yield i,tuple(sorted((i,)+tuple(j for j,b in zip(others,bits) if b)))

def enumerate_physical(mu,cases):
 paths=list(raw_paths(mu,cases));values=[]
 for mask in range(4):
  R=tuple(i for i in range(2) if mask>>i&1)
  for first in (None,)+R:
   E=tuple(i for i in range(2) if i!=first)
   observed={}
   for pr,th,ys,alive in paths:
    L=tuple(i for i in R if alive[2*i])
    obs=() if first is None or first not in L else ((first,ys[first]),)
    observed[(L,obs)]=tuple(final_plans(L,E))
   keys=tuple(observed)
   for choices in product(*(observed[k] for k in keys)):
    mapping=dict(zip(keys,choices));total=0.
    for pr,th,ys,alive in paths:
     val=0.
     for i,x in enumerate(cases):
      if i not in R:val+=physical_terminal(mu,i,(),cases,th)
      else:val-=float(x.d)
     if first is not None:val-=float(cases[first].c)
     L=tuple(i for i in R if alive[2*i])
     obs=() if first is None or first not in L else ((first,ys[first]),)
     second,R2=mapping[(L,obs)]
     for i in L:
      if i not in R2:val+=physical_terminal(mu,i,obs,cases,th)
      else:val-=float(cases[i].d)
     if second is not None:val-=float(cases[second].c)
     obs2=obs+(((second,ys[second]),) if second is not None and alive[2*second+1] else ())
     for i in R2:
      if alive[2*i+1]:val+=physical_terminal(mu,i,obs2,cases,th)
     total+=pr*val
    values.append((mask,first,str(mapping),total))
 return max(v[3] for v in values),values

def local_last_components(mu,L,E,cases,tax=F(0)):
 """Final-slot local game with public cross-information and fixed A priority."""
 gi=[g(mu,i,cases) if i in L else F(0) for i in range(2)]
 bs={i:(1-cases[i].h)*signal_mean(mu,i,i,cases)-cases[i].c-cases[i].d-gi[i] for i in L if i in E}
 def cross(j,i):return (1-cases[j].h)*(1-cases[i].h)*(signal_mean(mu,i,j,cases)-gi[j])-cases[j].d-cases[j].h*gi[j]
 release=max(F(0),cross(0,1)) if 0 in L and 1 in bs and bs[1]>tax else F(0)
 active=0 if 0 in bs and bs[0]-tax>0 and bs[0]-tax>=release else (1 if 1 in bs and bs[1]>tax else None)
 comps=list(gi)
 if active is not None:
  comps[active]+=bs[active]
  for j in L:
   if j!=active:comps[j]+=max(F(0),cross(j,active))
 return tuple(comps),active

def local_last(mu,L,E,cases,tax=F(0)):
 comps,active=local_last_components(mu,L,E,cases,tax)
 return sum(comps),active

def local_root(mu,cases,tax=F(0),priority_toll=F(0)):
 # Game tree at root: A claims, releases-and-retains, or acts-and-releases.
 # Then B chooses its own stop/retain/research action. The second slot is
 # governed by local_last_components. All moves and types are public.
 def value(mask,active):
  R=tuple(i for i in range(2) if mask>>i&1)
  E=tuple(i for i in range(2) if i!=active)
  comps=[g(mu,i,cases) if i not in R else -cases[i].d for i in range(2)]
  private=list(comps)
  if active is not None:comps[active]-=cases[active].c;private[active]-=cases[active].c+tax
  if active==0:private[0]-=priority_toll
  for prob,m,L,y in branches(mu,R,active,cases):
   future,selected=local_last_components(m,L,E,cases,tax)
   for i in range(2):
    comps[i]+=prob*future[i]
    private[i]+=prob*(future[i]-(tax if selected==i else 0))
  return {'mask':mask,'active':active,'components':tuple(comps),'private':tuple(private),'payoff':sum(comps)}
 # Order choices so exact ties retire B rather than retaining; A takes early
 # service on an own-payoff tie when available, as in the independent model.
 claims=[value(1,0),value(3,0)]
 retain=[value(1,None),value(3,1),value(3,None)]
 retire=[value(0,None),value(2,1),value(2,None)]
 routes=[max(opts,key=lambda r:r['private'][1]) for opts in [claims,retain,retire]]
 return max(routes,key=lambda r:r['private'][0]),routes

def dump(v):
 if isinstance(v,F):return {'exact':str(v),'decimal':float(v)}
 if isinstance(v,dict):return {k:dump(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [dump(x) for x in v]
 return v

if __name__=='__main__':
 cases=(Case(q=F(4,5),c=F(1),h=F(1,100)),Case(q=F(19,20),c=F(30),h=F(1,100)))
 scenarios=[('correlated',tuple(map(f,['.58','.02','.02','.38'])),cases),('perfect_correlation_zero_expiry',(F(3,5),F(0),F(0),F(2,5)),(Case(),Case(q=F(19,20),c=F(30)))),('independent_same_marginals',(F(9,25),F(6,25),F(6,25),F(4,25)),cases)]
 rows=[];policyrows=[];details={};checks=0
 for name,mu,xs in scenarios:
  best,roots=solve(mu,xs);ve,vals=enumerate_physical(mu,xs)
  assert abs(float(best['value'])-ve)<1e-8;checks+=1
  for rec in roots:
   enumroot=max(v[3] for v in vals if v[0]==rec['root_mask'] and v[1]==rec['root_active'])
   assert abs(float(rec['value'])-enumroot)<1e-8;checks+=1
  for rec in vals:policyrows.append([name,*rec])
  rows.append(dict(scenario=name,root_mask=best['root_mask'],root_active=best['root_active'],optimal_exact=str(best['value']),optimal=float(best['value']),policies=len(vals)))
  lr,lroutes=local_root(mu,xs)
  # The R1 charge computed from unchanged marginal priors ignores cross-information.
  bB=(1-xs[1].h)*signal_mean(mu,1,1,xs)-xs[1].c-xs[1].d-g(mu,1,xs)
  wB=max(F(0),(1-xs[1].h)*bB-xs[1].d-xs[1].h*g(mu,1,xs))
  toll=max(F(0),bB)-wB
  oldrule,_=local_root(mu,xs,priority_toll=toll)
  details[name]={'local_root':lr,'local_routes':lroutes,'R1_marginal_toll':toll,'R1_rule_payoff':oldrule['payoff'],'prior':mu,'cases':[asdict(x) for x in xs],'optimal':best,'root_candidates':roots}
  rows[-1].update(local_root_payoff=float(lr['payoff']),local_root_active=lr['active'],R1_rule_payoff=float(oldrule['payoff']),deadline0=float(sum(g(mu,i,xs) for i in range(2))),deadline1=float(local_last(mu,(0,1),(0,1),xs)[0]))
  # Inspect the supported branch: A signal 1 and both cases survive.
  py,m=posterior(mu,0,1,xs);G=sum(g(m,i,xs) for i in range(2));opt,opts=last(m,(0,1),(1,),xs)
  bi=(1-xs[1].h)*signal_mean(m,1,1,xs)-xs[1].c-xs[1].d-g(m,1,xs)
  C=(1-xs[0].h)*(1-xs[1].h)*(signal_mean(m,1,0,xs)-g(m,0,xs))-xs[0].d-xs[0].h*g(m,0,xs)
  local=local_last(m,(0,1),(1,),xs)
  details[name]['positive_signal_branch']={'probability_given_A_survival':py,'posterior':m,'B_own_gain':bi,'A_cross_gain':C,'joint_gain':opt[0]-G,'local_gain':local[0]-G,'last_optimal_plan':opt}
  if name=='correlated':
   assert best['root_active']==0 and best['root_mask']==3;checks+=1
   assert bi<0<C and opt[0]-G>0 and local[0]==G;checks+=1
   assert lr['payoff']<best['value'] and oldrule['payoff']<best['value'];checks+=1
   py0,m0=posterior(mu,0,0,xs);opt0,_=last(m0,(0,1),(1,),xs)
   assert opt0[1] is None;checks+=1
   # Credit equal to the other case's gain implements the positive branch.
   assert bi+max(F(0),C)>0;checks+=1
   for tax in [F(0),F(1),F(10),F(100)]:
    assert local_last(m,(0,1),(1,),xs,tax)[0]==G;checks+=1
  if name=='independent_same_marginals':
   assert C<=0;checks+=1
 (OUT/'correlated_details.json').write_text(json.dumps(dump(details),indent=2))
 with (OUT/'correlated_results.csv').open('w') as z:
  w=csv.DictWriter(z,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 with (OUT/'correlated_enumeration.csv').open('w') as z:
  w=csv.writer(z);w.writerow(['scenario','root_mask','root_active','last_policy_map','payoff']);w.writerows(policyrows)
 summary={'synthetic':True,'checks_passed':checks,'named_cases':len(scenarios),'total_policy_rows':len(policyrows),'exact_rational_solution':True,'independent_evaluator':'latent state x signal x expiry outcomes with contingent retention and action','includes_previously_researched_case_retained_for_cross_information':True,'no_simulation':True}
 (OUT/'correlated_validation.json').write_text(json.dumps(summary,indent=2))
 print(json.dumps(summary,indent=2))
 for row in rows:print(row)
 for name,rec in details.items():print(name,dump(rec['positive_signal_branch']))
