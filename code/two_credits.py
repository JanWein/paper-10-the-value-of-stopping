"""R3 exact two-credit frontier in the SAME correlated two-case/two-slot game.
Standard library only. No Monte Carlo, new queue or parameter-grid campaign.
The physical evaluator below uses exact latent-path arithmetic, not Bellman values.
Endpoint certificates plus convexity prove a continuum, not an interpolation grid.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import csv,json
import correlated_analysis as old
OUT=Path(__file__).resolve().parents[1]/'results';OUT.mkdir(exist_ok=True)
TH=tuple(product((0,1),repeat=2));S=F(99,100)
CASES=(old.Case(q=F(4,5),c=F(1),h=F(1,100)),old.Case(q=F(19,20),c=F(30),h=F(1,100)))
LO,HI=F(17,100),F(23,100)
D0,D1=F(7831,45000),F(5291,30000)
P=F(107811,250000)
def prior(d):return (F(9,25)+d,F(6,25)-d,F(6,25)-d,F(4,25)+d)
def targetA(d):return (43226820450*d+33275667541)/500000000
def targetB(d):return 297*(495000*d+515039)/2500000
def K(d):return (30000*d-5291)/220
def creditA(d):
 return ((877679550*d+171175559) if d<=D0 else (44982179550*d-7503987541))/500000000
def releaseA(d):return targetA(d)+creditA(d)
def implemented(d,C,k,strict=False):return C>=0 and k>=0 and (C>creditA(d) if strict else C>=creditA(d)) and k>K(d)
def budgets(d,strict=False):
 k=max(F(0),K(d));return {'expected_infimum':creditA(d)+P*k,'pathwise_infimum':creditA(d)+k,'attained':not strict and K(d)<0}

def budget_feasible(d,expected=None,capacity=None,strict=False):
 b=budgets(d,strict);weak=b['attained']
 return all(cap is None or (cap>=b[key] if weak else cap>b[key])
            for cap,key in [(expected,'expected_infimum'),(capacity,'pathwise_infimum')])

def final_local(mu,L,E,kappa=F(0),eligible=False):
 """All own stopping/research/passive-retention choices, with stipulated ties."""
 gi=[old.g(mu,i,CASES) if i in L else F(0) for i in range(2)]
 bs={i:S*old.signal_mean(mu,i,i,CASES)-CASES[i].c-gi[i] for i in L if i in E}
 def cross(j,i):return S*S*(old.signal_mean(mu,i,j,CASES)-gi[j])-F(1,100)*gi[j]
 credit=kappa if eligible else F(0)
 release=max(F(0),cross(0,1)) if 0 in L and 1 in bs and bs[1]+credit>0 else F(0)
 active=0 if 0 in bs and bs[0]>0 and bs[0]>=release else (1 if 1 in bs and bs[1]+credit>0 else None)
 resource=list(gi);private=list(gi);retained=[]
 if active is not None:
  resource[active]+=bs[active];private[active]+=bs[active]+(credit if active==1 else 0);retained=[active]
  for j in L:
   if j!=active and cross(j,active)>0:
    resource[j]+=cross(j,active);private[j]+=cross(j,active);retained.append(j)
 return tuple(resource),tuple(private),active,tuple(sorted(retained))

def game(d,C=F(0),kappa=F(0),toll=F(0)):
 """Recompute all eight roots with LOCAL continuation; never force dispatcher."""
 mu=prior(d);rows=[]
 for mask in range(4):
  R=tuple(i for i in range(2) if mask>>i&1)
  for first in (None,)+R:
   E=tuple(i for i in range(2) if i!=first)
   res=[old.g(mu,i,CASES) if i not in R else F(0) for i in range(2)];prv=list(res)
   if first is not None:res[first]-=CASES[first].c;prv[first]-=CASES[first].c
   if first==0:prv[0]+=C-toll
   hist=[]
   for prob,post,L,y in old.branches(mu,R,first,CASES):
    eligible=first==0 and L==(0,1) and y=='1'
    r,v,active,ret=final_local(post,L,E,kappa,eligible)
    for i in range(2):res[i]+=prob*r[i];prv[i]+=prob*v[i]
    hist.append({'probability':prob,'live':L,'signal':y,'eligible':eligible,'active':active,'retained':ret,'resource':r,'private':v})
   rows.append({'mask':mask,'first':first,'resource':tuple(res),'private':tuple(prv),'history':hist})
 def pick(keys):return max([next(r for r in rows if (r['mask'],r['first'])==k) for k in keys],key=lambda r:r['private'][1])
 routes=[pick([(1,0),(3,0)]),pick([(1,None),(3,1),(3,None)]),pick([(0,None),(2,1),(2,None)])]
 return max(routes,key=lambda r:r['private'][0]),routes,rows

# Separate physical policy enumeration, all arithmetic exact. No use of old.g,
# old.posterior, old.last, old.solve or old.branches in the evaluator below.
def paths(mu):
 for theta,p in zip(TH,mu):
  for ys in product((0,1),repeat=2):
   z=p
   for i,q in enumerate((F(4,5),F(19,20))):z*=q if ys[i]==theta[i] else 1-q
   for alive in product((0,1),repeat=4):
    z2=z
    for a in alive:z2*=S if a else 1-S
    if z2:yield z2,theta,ys,alive

def reward(mu,i,obs,theta):
 weights=list(mu)
 for k,y in obs:
  q=(F(4,5),F(19,20))[k]
  weights=[w*(q if t[k]==y else 1-q) for t,w in zip(TH,weights)]
 p1=sum(w for t,w in zip(TH,weights) if t[i]);p0=sum(w for t,w in zip(TH,weights) if not t[i])
 return F(100) if int(p1>=p0)==theta[i] else F(0)

def plans(L,E):
 yield None,()
 for active in L:
  if active in E:
   other=tuple(i for i in L if i!=active)
   for bits in product((0,1),repeat=len(other)):
    yield active,tuple(sorted((active,)+tuple(i for i,b in zip(other,bits) if b)))

def physical_enumeration(d):
 mu=prior(d);raw=list(paths(mu));records=[]
 # Precompute rewards independently from Bayes formulas for cheap exact sums.
 rewards={}
 for _,theta,ys,_ in raw:
  for obs in [(),((0,ys[0]),),((1,ys[1]),),((0,ys[0]),(1,ys[1])),((1,ys[1]),(0,ys[0]))]:
   for i in range(2):rewards[(theta,i,obs)]=reward(mu,i,obs,theta)
 for mask in range(4):
  R=tuple(i for i in range(2) if mask>>i&1)
  for first in (None,)+R:
   E=tuple(i for i in range(2) if i!=first);nodes={}
   for _,theta,ys,alive in raw:
    L=tuple(i for i in R if alive[2*i]);obs=() if first is None or first not in L else ((first,ys[first]),)
    nodes[(L,obs)]=tuple(plans(L,E))
   keys=tuple(nodes)
   # Aggregate each history/plan's unconditional physical component once.
   const=[F(0),F(0)];tails={}
   for key in keys:
    for plan in nodes[key]:tails[(key,plan)]=[F(0),F(0)]
   for prob,theta,ys,alive in raw:
    L=tuple(i for i in R if alive[2*i]);obs=() if first is None or first not in L else ((first,ys[first]),)
    key=(L,obs)
    for i in range(2):
     if i not in R:const[i]+=prob*rewards[(theta,i,())]
     if i==first:const[i]-=prob*(1 if i==0 else 30)
    for plan in nodes[key]:
     active,retained=plan;obs2=obs+(((active,ys[active]),) if active is not None and alive[2*active+1] else ())
     for i in L:
      v=F(0)
      if i not in retained:v+=rewards[(theta,i,obs)]
      elif alive[2*i+1]:v+=rewards[(theta,i,obs2)]
      if active==i:v-=1 if i==0 else 30
      tails[(key,plan)][i]+=prob*v
   for choices in product(*(nodes[k] for k in keys)):
    v=list(const)
    for key,plan in zip(keys,choices):
     for i in range(2):v[i]+=tails[(key,plan)][i]
    records.append({'mask':mask,'first':first,'mapping':str(dict(zip(keys,choices))),'components':tuple(v),'total':sum(v)})
 return records

def encoded(x):
 if isinstance(x,F):return {'exact':str(x),'decimal':float(x)}
 if isinstance(x,dict):return {str(k):encoded(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encoded(v) for v in x]
 return x

if __name__=='__main__':
 checks=0;certificate=[];rows=[]
 for d in [LO,F(11,50),HI]:
  recs=physical_enumeration(d);best=max(recs,key=lambda r:r['total'])
  assert len(recs)==63;checks+=1
  assert best['mask']==3 and best['first']==0;checks+=1
  assert best['components']==(targetA(d),targetB(d));checks+=1
  assert sum(r['total']==best['total'] for r in recs)==1;checks+=1
  target=targetA(d)+targetB(d)
  roots=[]
  for mask in range(4):
   for active in (None,)+tuple(i for i in range(2) if mask>>i&1):
    val=max(r['total'] for r in recs if r['mask']==mask and r['first']==active)
    roots.append({'mask':mask,'active':active,'value':val,'target_gap':target-val})
    if (mask,active)!=(3,0):assert val<target;checks+=1
  certificate.append({'delta':d,'target_components':best['components'],'roots':roots})
  for r in recs:rows.append([str(d),r['mask'],r['first'],r['mapping'],str(r['components'][0]),str(r['components'][1]),str(r['total'])])
  # Test a concrete implemented policy without forcing any local choice.
  C=creditA(d);k=max(F(0),K(d))+F(1,100)
  chosen,routes,allroots=game(d,C,k)
  assert chosen['mask']==3 and chosen['first']==0;checks+=1
  assert chosen['resource']==best['components'];checks+=1
  for h in chosen['history']:
   expected=1 if (h['live']==(1,) or (h['live']==(0,1) and h['signal']=='1')) else None
   assert h['active']==expected;checks+=1
  assert routes[1]['resource'][0]==releaseA(d);checks+=1
  assert routes[0]['private'][0]==routes[1]['private'][0];checks+=1
  assert routes[0]['private'][1]==targetB(d)+P*k>60;checks+=1
  assert routes[1]['private'][1]==F(1281,20);checks+=1
  # Necessary inequalities fail at the exact boundaries, never via a fee grid.
  bad,_,_=game(d,C-F(1,100000),k)
  assert bad['first']!=0;checks+=1
  if K(d)>=0:
   bad,_,_=game(d,C,K(d));hist=next(h for h in bad['history'] if h['eligible']) if bad['first']==0 else None
   assert hist is None or hist['active'] is None;checks+=1
  _,troutes,_=game(d,F(0),k,toll=F(1))
  assert troutes[0]['private'][0]<troutes[1]['private'][0];checks+=1
 # Exact endpoint ties and funding attainment.
 assert (877679550*D0+171175559)==(44982179550*D0-7503987541);checks+=1
 assert K(D1)==0;checks+=1
 for d in [LO,D0,D1,F(11,50),HI]:
  threshold=max(F(0),K(d));chosen,rs,_=game(d,creditA(d),threshold)
  assert implemented(d,creditA(d),threshold)==(d<D1);checks+=1
  if d<D1:
   assert chosen['first']==0 and chosen['resource']==(targetA(d),targetB(d));checks+=1
  else:
   assert not (chosen['first']==0 and chosen['resource']==(targetA(d),targetB(d)));checks+=1
 d=F(11,50);C=creditA(d);k=K(d);bd=budgets(d)
 assert targetA(d)==F(1069639201,12500000);checks+=1
 assert C==F(59802299,12500000);checks+=1
 assert k==F(119,20);checks+=1
 assert bd['expected_infimum']==F(183752143,25000000);checks+=1
 assert bd['pathwise_infimum']==F(134177299,12500000);checks+=1
 assert targetB(d)+P*k==F('76.689855');checks+=1
 assert not budget_feasible(d,expected=bd['expected_infimum']);checks+=1
 assert not budget_feasible(d,capacity=bd['pathwise_infimum']);checks+=1
 assert budget_feasible(d,expected=bd['expected_infimum']+F(1,100),capacity=bd['pathwise_infimum']+F(1,100));checks+=1
 assert budget_feasible(LO,expected=creditA(LO),capacity=creditA(LO));checks+=1
 assert not budget_feasible(LO,expected=creditA(LO),strict=True);checks+=1
 assert not budget_feasible(D1,expected=creditA(D1));checks+=1
 selected,routes,rootrows=game(d,C+F(1,100),k+F(1,100))
 (OUT/'two_credit_certificate.json').write_text(json.dumps(encoded({'synthetic':True,'interval':[LO,HI],'breakpoints':{'release_experiment_tie':D0,'credit_zero_tie':D1},'event_probability':P,'endpoint_and_witness_certificate':certificate,'witness_strict_game':{'selected':selected,'routes':routes,'all_roots':rootrows},'witness_infima':bd,'frontier':'C>=F(delta), kappa>=0, kappa>K(delta); strict root C>F(delta)','expected_budget':'C+p*kappa','pathwise_capacity':'C+kappa','exact_arithmetic':True}),indent=2))
 with (OUT/'two_credit_physical_enumeration.csv').open('w') as f:
  w=csv.writer(f);w.writerow(['delta','root_mask','first','last_mapping','A_resource','B_resource','total_resource']);w.writerows(rows)
 result={'checks_passed':checks,'physical_policy_rows':len(rows),'certificate_priors':3,'parameter_grid':False,'exact_physical_arithmetic':True,'scope':'Closed interval proved by affine target and convex competitors, not a sampled-prior claim'}
 (OUT/'two_credit_validation.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));print(json.dumps(encoded(bd),indent=2))
