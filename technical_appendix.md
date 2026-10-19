---
title: 'Paper 10 R1: Technical Appendix'
date: '17 October 2026'
geometry: margin=1in
---

# Appendix A. Shared-resource model: complete derivations and verification

## A.1 Binary signal and posterior actions

For case i with prior p and accuracy q, the joint probabilities of state 1 and signal 1, state 0 and signal 1 are pq and (1-p)(1-q). The joint probabilities for signal 0 are p(1-q) and (1-p)q. Bayes-optimal expected classification accuracy is

$$a(p,q)=\max\{pq,(1-p)(1-q)\}+\max\{p(1-q),(1-p)q\}.$$

Thus $\bar m=1-a(p,q)$ and $M=S[r+(1-r)a(p,q)]$. At any zero-probability signal branch, the posterior action is irrelevant to the expected payoff. At a posterior tie either terminal action has the same value. The enumeration uses a fixed state-1 tie convention. The formula applies to asymmetric priors without presuming that the signal always overturns the prior-optimal action.

## A.2 Deferred value and no double counting

If the case acts now, it receives g. If it waits one slot before deciding whether to research, it incurs d immediately; expiration destroys the opportunity with probability h. Conditional on survival the last-slot optimal value is $g+b^+$. Waiting's incremental payoff is

$$-d+s(g+b^+)-g=-\ell+sb^+.$$

The best of action now and this option gives $[-\ell+sb^+]^+$. Since $\ell\geq0$, this equals $[sb-\ell]^+$ for every real b, which is w. In particular, w>0 implies b>0. The expression includes the cost of the later experiment through b, the first waiting slot's cost through ell, and two distinct opportunities for expiration through s and b. It does not charge a separate hypothetical missed opportunity in addition to those losses.

For i first and j waiting, a direct physical-outcome calculation gives

$$s_iM_i-c_i-d_i-d_j+s_j(s_jM_j-c_j-d_j).$$

Subtract $g_i+g_j$ and rearrange to $b_i+s_jb_j-\ell_j$. If waiting j is not profitable, immediately act on j and obtain $G+b_i$. Taking their maximum yields $G+b_i+w_j$. This identity is checked by the independent latent-outcome evaluator, not assumed in that evaluator.

## A.3 Exhaustiveness of Theorem 1

At the initial boundary there are four retained subsets, including the empty one. For each retained subset R, the active choice is one case in R or no research. Cases outside R act immediately. If some case is active, its experiment uses its only research opportunity; if it survives, action immediately after its signal weakly dominates further waiting because no additional own-state information or reward becomes available. The independent state assumption means its public signal cannot improve the remaining case's posterior. Therefore the only remaining decision is whether an unserved case was retained and, if it survived, whether to research it in the last slot. This gives the two research-first candidates in Theorem 1, with optional immediate retirement of the unserved case embedded in w.

If no case is active initially, fix the retained subset R. Its expected value relative to immediate action on all cases is

$$-\sum_{i\in R}\ell_i+E\max\{0,\{b_i:i\in R\text{ survives}\}\}.$$

The expectation is bounded above by $\max(0,b_A,b_B)$. Immediate research on a positive maximizer, if one exists, followed by immediate action on the other case attains that upper bound without incurring the idle waiting losses. If none exists, stopping both dominates idling. This proves exhaustion even for policies that idle while retaining only one case. Signal-dependent final research choices cannot improve on w, because the other case's independent signal changes neither b nor the feasible final choices.

For both b positive, order comparison is exactly

$$[b_A+w_B]-[b_B+w_A]=u_A-u_B.$$

When b is nonpositive, that case's w is zero and it never needs research; Theorem 1's maximum also captures these corners. A case with h=0,d=0 can be deferred without loss. This yields payoff ties, not a failure of the formula.

## A.4 Sequential equilibrium with a common charge

The game is complete information. At the final slot each surviving case researches only if its charged gain b-tau is strictly positive. At the initial boundary A moves first. If A researches now, B's best wait gain is $[s_B(b_B-\tau)-\ell_B]^+$ and its alternative is immediate action. If A releases, B researches immediately whenever $b_B-\tau>0$; otherwise it acts. In the latter event A cannot gain by idling instead of taking its own available experiment immediately. If A releases to a researching B, its best waiting gain is $[s_A(b_A-\tau)-\ell_A]^+$.

For b_A-tau>0, its own immediate gain minus the untruncated deferred gain is

$$h_A(b_A-\tau)+\ell_A\geq0.$$

Truncating a negative deferred gain at zero preserves weak preference for immediate research. It is strict when ell_A>0. If both h_A and ell_A are zero, early and late gains tie and the stated early-service convention selects the first slot. For b_A-tau<=0, immediate action weakly dominates both research and waiting; the research-action tie convention selects action. Backward induction therefore yields Theorem 2, including off-path choices.

The actual firm payoff for b_A>tau is

$$G+b_A+\mathbf 1\{s_B(b_B-\tau)>\ell_B\}\,w_B.$$

The charge affects the private choice but is not subtracted again from social payoff. For b_A<=tau it is $G+\mathbf 1\{b_B>\tau\}b_B$. These formulas permit evaluation of all tau, not just sampled values.

## A.5 Full implementation classification and tie boundaries

Assume first that the efficient first research assignment is unique. If A first is optimal, b_A>0 and tau=0 reproduces its efficient retention decision for B. If B first is optimal and b_A<=0, tau=0 implements it. If neither case has positive b, acting immediately is efficient and tau=0 implements it.

The remaining case has unique B first and b_A>0. If w_A=0, strict optimality implies b_B>b_A+w_B>=b_A. A releases and stops for tau>=b_A, while B researches for tau<b_B; hence [b_A,b_B) is sufficient and, under the early-service convention, necessary. If w_A>0, tau<b_A preserves A's first claim and tau>=b_A destroys its later research incentive. Thus no tau works under that convention. With ell_A>0 this conclusion is independent of first-slot tie-breaking because A strictly prefers early service for every tau<b_A.

If ell_A=0, h_A=d_A=0 because g_A>0. For tau<b_A A can be indifferent between early and late service. Selecting release in that tie can support the efficient B-first route. The stronger claim that *no equilibrium with any tie-breaking* implements the optimum would therefore be false. We do not make it. At ties in the joint optimum, implementation requires attaining any joint-optimal policy, not a predetermined labeled ordering. The formulas in the main text directly test such cases.

A common deadline can leave zero, one, or two slots because the model is discrete. Equation (5) is the exhaustive equilibrium payoff list for an unpriced unchanged priority game. A strict B-first optimum with b_A>0 exceeds all three. If deadline design includes changing priority rights, case-specific deadlines, or contingent exceptions, it is outside this impossibility statement.

## A.6 Opportunity-loss pricing and transfers

Corollary 2 follows because a fixed first-slot fee k induces the same comparison $b_A-k$ versus w_A in every rival state. With A fixed and both rivals willing to use a released slot, low and high rival deferral losses that straddle u_A require opposite strict inequalities on k. In the synthetic belief example, changing only B's prior from .5 to .705 changes its loss from 14.2 to .5, straddling u_A=1.352.

The posted first-slot charge for A is $u_B=b_B^+-w_B$. If both cases have positive b, A compares its early gain $b_A-u_B$ with its release-and-retain gain w_A. The difference is u_A-u_B. B's first-service and deferred-service choices are uncharged, so b_B and w_B are undistorted. The resulting joint policy selects exactly a maximizing route in Theorem 1. The same argument applies if A immediately acts after release because w_A=0.

If b_B<=0, u_B=w_B=0, B immediately acts. A's early versus deferred comparison is b_A versus w_A. If these tie at a positive value, A has h_A=d_A=0, so waiting and using the otherwise idle final slot is payoff equivalent. If b_A<=0 it cannot obtain positive gain by claiming or waiting. Both nonpositive cases stop. This proves all corners of Theorem 3.

The charge equals the change in B's optimal incremental payoff between being offered first service and being offered deferred service. It is not B's gross reward or all of its evidence value. A central budget can retain it. The implementation claim assumes marginal booked transfers enter objectives and cannot be evaded; it does not establish budget balance, individual participation relative to every alternative institutional entitlement, or private-type revelation. The general dynamic-pivot literature is therefore a precedent, not a theorem proved anew here.

## A.7 Comparative statics and a reversed order

Let delta=m-mbar>=0. At fixed signal law,

$$\partial_r b=sS\bar m-Sm=-S(\delta+h\bar m).$$

Within b>0,w>0,

$$u=b-(sb-\ell)=hb+\ell=hsM-hc+sd,$$

so $\partial_r u=hsS\bar m$. At p=.5,q=.7,S=100,c=1,d=0,h=.02, b(r)=17.6-20.6r and u(r)=1.352+.588r on this interior segment. At r=.5, b=7.3,w=5.654,u=1.646. A fixed rival u=1.48412 is crossed at r approximately .22469, inside the region where deferred research remains profitable. The exact crossing is (1.48412-1.352)/.588. All reported endpoints and ordering are in the generated output.

For other parameters within this region, $\partial_S u=hs[1-(1-r)\bar m]>0$ when h>0, whereas $\partial_S b=s[1-(1-r)\bar m]-[1-(1-r)m]$ may have either sign. Increasing signal informativeness lowers mbar and raises M; its effect on b and, in this interior, u is nonnegative. The hazard derivative of u is $(1-2h)M-c-d$, which need not be positive. Near a stopping boundary, positive-part kinks require evaluating the piecewise formula, not extrapolating derivatives. These statements do not extend without modification to trials, state-dependent expiration, correlated cases, or multiple remaining signals.

## A.8 Independent enumeration: policies and physical paths

The enumerator and closed-form solver share primitive inputs only. It enumerates theta_A,theta_B; one potential binary signal for each case; and two potential survival coins per case. Unused draws integrate out. Actual action success or error is evaluated against the latent state; costs are charged only when a case is retained or researched. A case stopped at intake earns its actual prior-optimal action payoff on that latent path, not zero. A case expiring before action receives zero terminal reward.

For strictly interior hazards, the eight root actions are: stop both; retain A with active A or no research; retain B with active B or no research; retain both with A active, B active, or no research. Their feasible final-slot contingent policies number 1,1,2,1,2,8,8,12, respectively, totaling 35. For root A-active with both retained, A has three public outcomes (expiry, signal 0, signal 1); for each, if B survives the policy can act or research B. Thus there are 2^3=8 maps, even though independence ultimately makes their optimal choices the same across A's outcomes. For root idle-both, the both-survive node allows three final assignments and each one-survive node two; the neither-survive node has one, giving 3*2*2=12. Zero-probability nodes are removed, reducing counts in boundary cases.

All positive-probability latent/signal/hazard paths are integrated for each map. The maximum is compared with Theorem 1. The code also compares the posted rule with the optimum over a deterministic parameter grid, verifies local payoff does not exceed it, and checks the charge-failure and recoverability examples. New validation output reports 250 checks; these are computational tests, not additional formal results or estimated observations. The primitive grid is deliberately heterogeneous and is not a calibration. Complete named-scenario policy rows are supplied in CSV, including dominated idle policies.

## A.9 Conditional valuation bounds

For an implemented fixed joint policy z, expected total payoff can be written $A_z-\sum_i d_iT_{iz}$, where A includes terminal rewards and acquisition expenses, and T_i is expected unresolved case-period exposure. Expiration is already inside A and T. Holding intervals $d_i\in[l_i,u_i]$ give endpoint bounds for each fixed-policy contrast by selecting endpoints according to the signs of the exposure differences. Do not add u_i as another resource expense.

If priors, precision, stakes, recoverability, or hazards are uncertain, these quantities and even the optimal policy change. A cost-only endpoint calculation holds them fixed. For a full uncertainty set Omega, a proposed fixed policy is certified over a comparator set only if the minimum of each payoff contrast over Omega is nonnegative. Without a justified Omega and actual parameter restrictions there is no claim of model robustness. The paper implements synthetic point-primitives only.

# Appendix B. Retained separable benchmark and previous checks



## B.1 Existence, admissibility, and the cost frontier

The finite history tree has finitely many actions at each node. A deterministic strategy assigns stop-and-act or an experiment to each live nonterminal node. Backward induction gives an optimal deterministic strategy for every cost price $b$. Randomized strategies are mixtures and cannot exceed the best deterministic expected payoff. All rewards and costs are bounded because the tree is finite.

Fix a live history $x$ and a deterministic strategy $\pi$ constrained to continue first. Let $\tau$ count the number of research choices before terminal action or expiration. Expected resource expense is $C_\pi=E_\pi\sum_{s<\tau}c_s$. Delay exposure is $T_\pi=E_\pi\tau\geq1$. Let $R_\pi$ count the action reward only on histories where action precedes expiration. Then

$$J_b(\pi)-g(x)=R_\pi-C_\pi-g(x)-bT_\pi.$$

The maximum over $\Pi^+$ is strictly positive if and only if $b$ is below the maximum ratio. A negative ratio means that strategy is inferior even with free additive delay. When $b$ equals the largest ratio, stopping ties with a best continuation and is selected by convention. At histories where continuation is impossible use $D=-\infty$. The binary continuation region is nested in $b$, even though the optimal experiment need not remain the same. This proof does not rely on a Gaussian posterior, stationary boundaries, or a one-signal approximation.

## B.2 Bellman regret identity

For a continuation action $e$ let

$$Q_d(x,e)=-c_e-d+(1-h_e)E_e V_d(x').$$

For a terminal action $a$, let $Q_d(x,a)=E[u(a,\theta,x)\mid x]$. Optimal action payoff $g$ is the maximum over terminal actions. Extend $V$ by zero to the absorbing expired state. At a live continuation state, the realized period reward is $-c_e-d$. Its conditional expectation plus the next-state value equals $Q_d$. At a terminal state, realized terminal reward has conditional expectation $Q_d(x,a)$ and next value zero.

Subtract the conditional equality from $V_d(x)$, sum along the realized finite path, and apply iterated expectations. Intermediate values cancel. The initial value minus all expected realized rewards is the expected sum of $V_d-Q_d$. This yields the formula in separable benchmark. There is no survival conditioning or exclusion of incomplete cases. A deadline alters $\mu$ at every history where its anticipation changes behavior, and the identity still holds.

## B.3 State-specific stopping interventions

Let $\mu$ be the original analyst policy evaluated at firm costs. At every selected history $x$ with $V_d(x)=g(x)$, $J_d(\mu\mid x)\leq g(x)$. Changing the policy to stop there gives at least its old continuation value. At unselected histories retain the old action. By induction from terminal histories, improvements in successor continuation values weakly improve predecessor payoffs, while selected histories weakly improve because no feasible continuation beats $g$. Thus expected firm payoff cannot fall. If some selected reachable history had a strictly negative old continuation gain and is reached with positive probability under the new prefix, the improvement is strict. This argument presumes fixed signal technology and no queue or effort response.

## B.4 Worked nonmyopic example

Let current probability of state 1 be .7, signal accuracy .7, no expiration, correct action reward 100, wrong action zero. One positive signal has probability .58 and posterior $.49/.58$; a negative signal has probability .42 and posterior .5. Expected maximum posterior is $.49+.21=.70$. Immediate one-step value of information is zero.

Two further signals yield unconditional state-likelihood pairs: positive-positive $(.343,.027)$; each mixed path $(.147,.063)$; negative-negative $(.063,.147)$. Summing maxima gives $.343+2(.147)+.147=.784$. Two samples cost two when $c=1,d=0$, so a feasible continuation gains 6.4. This is a lower bound on optimal adaptive continuation value, sufficient to disprove the myopic converse. The delivered code checks the posterior arithmetic independently of the Bellman recursion.

## B.5 Final-period derivation and boundaries

Expected payoff after one experiment followed by action is $(1-h)(S-L\bar m)-c-d$. Subtract $S-Lm$. Rearrangement yields $(1-h)L(m-\bar m)-h(S-Lm)-c-d$. Blackwell precision lowers expected Bayes classification error at fixed prior and payoff. Hazard lowers the value through both foregone learning and destruction of immediate opportunity value. The derivative with respect to $r$ is nonpositive even though wrong-action salvage increases the level of immediate reward.

Higher stakes do not universally favor waiting. For example, at prior .5, $r=0,q=.55,h=.2$, the coefficient of $S$ is $.8(.55)-.5=-.06$. With nonnegative costs, continuation is inferior at every positive stake. Here greater stakes increase the value destroyed by expiration faster than the value of learning. This is consistent with the reported high-hazard scenario, but is a separate final-period analytical example.

## B.6 Delay-cost uncertainty and policy ranking

For fixed policies $z=0,1$, define $A_z=R_z-C_z$, so $W_z(d)=A_z-dT_z$. For $d\in[d_L,d_U]$, the contrast interval is

$$[\min\{\Delta A-d_L\Delta T,\Delta A-d_U\Delta T\},
\max\{\Delta A-d_L\Delta T,\Delta A-d_U\Delta T\}].$$

If $\Delta T=0$, delay price cannot change the ranking. Otherwise the break-even price is $\Delta A/\Delta T$, which need not lie in the admissible interval. This formula values fixed implemented policies. It is distinct from optimizing $V_d$ separately for every price.

With heterogeneous $d_i\in[l_i,u_i]$, use case-level extrema of $A_i-d_iT_i$. For a treatment-control difference, subtract the control upper bound from the treatment lower bound for the lower contrast, and conversely for the upper. This is conservative when cross-case cost restrictions are ignored. It does not identify a missing payoff component merely because its interval is assigned a number.

## B.7 Optional stopping and inference

The model is a Bayesian economic stopping problem, not repeated null-hypothesis testing. No signal is a sequence of unadjusted p-values. The proposed trial uses a fixed final analysis date and fixed enrollment after feasibility. Exploratory interim monitoring cannot trigger an ordinary fixed-sample significance claim. If operational needs require sequential confirmatory monitoring, an alpha-spending plan or an always-valid method and its assumptions must be chosen and registered before treatment outcomes are examined. No sequential frequentist method is implemented in this package.

## B.8 Computational verification

Python 3 standard-library code implements exact posterior updating on $(n,k)$, backward induction under perceived costs, and separate forward evaluation at full costs. In the pre-R1 separable implementation, 12,002 assertions/checks pass. The parameter-grid count is 324: three stakes, three recovery fractions, three precisions, four delay prices, and three hazards. Each compares all 36 nonterminal histories of an eight-period tree and the initial welfare ordering, yielding 11,988 checks. Seven frontier comparisons, three posterior checks, and four derivatives give 12,002 total. The posterior pair calculation is one of the three posterior checks.

For an independent check, the script enumerates all distinct pairs $(R-C,T)$ at horizon three, allowing independent policy choices at the two signal descendants. It retains 15 distinct pairs at the root and verifies their upper envelope against the Bellman solution. This is numerical agreement with a finite tree, not a proof for an infinite horizon. The policy CSV uses a 12-period horizon. Floating-point comparisons use tolerances; no random seed is required.

\newpage

# Appendix C. Earlier single-case synthetic illustrations

These are retained separable benchmarks, not evidence for the shared-resource mechanism. The prior is .5, signal accuracy .7, correct payoff 100, wrong payoff zero, acquisition cost 1, additive delay cost 5, expiration probability .02 per research period, and a 12-sample finite horizon. The silo internalizes ten percent of additive delay cost. Values are arbitrary model units, computed by exact backward induction and separate full-cost policy evaluation.

\begin{center}
\small
\begin{tabular}{@{}p{2.55in}rrrr@{}}
\toprule
Policy or environment & Payoff & Periods & Complete & Accuracy \\
\midrule
Firm optimum & 62.600 & 1.000 & .980 & .700 \\
Silo analyst & 59.002 & 3.294 & .934 & .843 \\
Silo, immediate deadline & 50.000 & 0.000 & 1.000 & .500 \\
Silo, one-sample deadline & 62.600 & 1.000 & .980 & .700 \\
Silo, four-sample deadline & 60.430 & 2.383 & .952 & .785 \\
Firm, minimum two samples & 60.430 & 2.383 & .952 & .785 \\
Firm, recoverable share .8 & 90.000 & 0.000 & 1.000 & .500 \\
Silo, recoverable share .8 & 86.120 & 1.000 & .980 & .700 \\
Firm, correct payoff 500 & 374.065 & 3.294 & .934 & .843 \\
Firm, expiration hazard .20 & 50.000 & 0.000 & 1.000 & .500 \\
\bottomrule
\end{tabular}
\end{center}

Accuracy is conditional on completion. Payoff and completion include every opportunity. Relative to the silo policy, a one-sample deadline raises total payoff by 3.598 despite lowering completed-case accuracy. An immediate deadline lowers payoff to 50. A mandatory second sample can reduce value by making the intermediate work compulsory while leaving further continuation endogenous.

The executed legacy script independently checks a three-period payoff/time frontier against backward induction, verifies continuation-set nesting on a grid, and checks the nonmyopic counterexample and final-period derivatives. It reports 12,002 checks. These results neither identify firm behavior nor establish a novel single-case index.

The fixed-policy delay-price file separates gross reward less acquisition expense from active-period exposure. Its break-even comparison for the frozen one-sample and silo policies is approximately 3.432 delay-cost units. Those bounds hold the full signal/reward/expiration model and implemented policies fixed. Reoptimizing at each price answers another question.

The horizon is a substantive finite assumption, not an unverified infinite-horizon approximation. The R1 main model instead has exactly two cases, one experiment each, and two slots.

\newpage

# Appendix D. Correlated two-case/two-slot extension: complete details

## D.1 Probability space and filtration

The latent state vector takes values (0,0),(0,1),(1,0),(1,1) with public prior mu. Each case has one potential binary signal, conditionally independent given that vector, with likelihood q_i for a correct signal. There are two potential independent survival coins for each case, independent of the states and signals. A survival coin is used only when that case is unresolved across that slot. The potential signal is observed only when its experiment is conducted and its case survives the corresponding slot. Unused draws integrate out. No latent outcome of an irrevocable terminal action is revealed during the window; realization is settled later. This is essential to avoiding unmodeled free information from action outcomes.

The filtration consists of all observed research assignments, stops, survival events, and delivered signals. Expiry itself is uninformative about latent types. For any nonzero-probability observed signal y from case k,

$$\mu^{k,y}_{ab}=\frac{\mu_{ab}\Pr(y\mid\theta_k)}{\sum_{a',b'}\mu_{a'b'}\Pr(y\mid\theta_k')}.$$

All continuing policies are adapted to this public filtration. At most two experiments occur in total, never more than one on a particular case. Case payoffs remain additive even though their conditional expectations respond to common information.

## D.2 Final-slot formula

Fix the current posterior, live set L, and unused-experiment set E. Stopping every case gives $G_L=\sum_{i\in L}g_i$. If k is researched, its own expected resource payoff is $-c_k-d_k+s_kM_{k|k}$, a gain b_k. A passive case i may stop for g_i or remain unresolved across the slot. If retained, its expected payoff is

$$-d_i+s_i[(1-s_k)g_i+s_kM_{i|k}].$$

Subtracting g_i gives

$$-d_i-h_ig_i+s_is_k(M_{i|k}-g_i)=a_{i|k}.$$

This accounts separately for expiry of the recipient and nonarrival of the source signal. Their hazards are independent, even though the latent states are correlated. The optimal retention gain is a^+. Summing this and b_k, and taking the best single k or stopping all, proves equation (9). A previously used case may be a recipient and therefore belongs in L even if absent from E. This is the key difference from the independent-case enumeration.

If no experiment is selected in the final slot, waiting creates no signal or action improvement; holding costs and expiry cannot improve nonnegative expected terminal rewards. Thus final idle policies are weakly dominated. All researched and retained survivors choose Bayes-optimal terminal actions after the selected signal, if delivered. No retrospective reuse of a future signal is allowed for a case that acted before it.

## D.3 Initial action exhaustion and rational solution

There are four retained subsets R. When R is empty there is one active choice; for each singleton R there are two (no research or that case); when both are retained there are three. The total is eight. Every case outside R locks its immediate-action payoff and can neither be reopened nor researched later. Every case in R pays d_i for this slot, and a selected experiment pays c_k once whether or not its case survives. Conditional on survivors, if k survived, Bayes-update on its signal; if not, do not update. These are exactly the terms in (10).

The remaining value is explicitly (9), so (10)-(11) are a finite closed evaluation of eight rational expressions with maxima, not an unsolved infinite or general queue recursion. Posterior probabilities and signal probabilities are rational whenever the primitives are rational. The supplied solver uses Fraction arithmetic throughout this calculation.

Under independence, the passive mean $M_{i|k}$ equals g_i. Thus passive research-information retention in the last slot is dominated, including for the previously studied case. The unused case's posterior is unchanged by the first signal. If scheduled second its optimal initial retention gain is the independent w_i, so the eight-action formula reduces to Theorem 1, with initial idle options dominated as already proved. This verifies preservation of the original 137.248 independent example; the correlated model does not replace its assumptions retroactively.

## D.4 Complete local game

At one remaining slot, define charged own research gains $b_i-\tau$. If B has an experiment and $b_B>\tau$, A's own best release-and-learn gain is $a_{A|B}^+$; otherwise it is zero. If A also has an experiment it claims research precisely when its charged own gain is positive and weakly exceeds that release gain. A positive tie between early research and later free learning favors its priority claim; a zero tie favors immediate action. If A releases or has no experiment, B researches iff $b_B>\tau$. Given the active case, each passive owner retains iff its own a is positive; otherwise it acts before the signal. These are optimal local actions because passive retention does not alter the active owner's own signal or resource costs. If no case researches, both act.

Let the resulting two components be $L_i^1(\mu,L,E;\tau)$, expressed at full resource costs without subtracting transfers. For a root choice (R,k), the actual component is

$$Q_i^L(R,k)=\mathbf1\{i\notin R\}g_i
-\mathbf1\{i\in R\}d_i-\mathbf1\{k=i\}c_i
+E[L_i^1(\mu',L',E_k;\tau)].$$

The private component subtracts the root experiment charge and expected future experiment charge, each paid only by the active owner. If a priority toll is applied only when A claims the initial slot, subtract it only from A's private component on that branch. The transfer is never subtracted from total resource payoff.

B's follower alternatives after A claims are its immediate action or retention, giving the set C. If A releases and stays unresolved, B can act, research now, or wait, giving R. If A acts and releases, B has the same three own choices with A removed, giving X. These sets of size 2,3,3 exhaust the eight feasible root actions. Choose B's highest private component in each set, then A's highest private component among the three resulting routes. This is full backward induction of the finite perfect-information local game, including off-path choices. No equilibrium is inferred from a joint-optimal dispatcher policy.

In the full-support synthetic example, at zero charge the three locally optimal route pairs (A resource payoff, B resource payoff) are:

- A claims, B retains: (78.2, 76.689855).
- A releases and stays, B researches: (90.35532, 64.05).
- A acts and releases, B researches: (60, 64.05).

A therefore releases and stays, so the local total is 154.40532. Its claim route has total 154.889855 but is privately worse for A. Even that route does not achieve the efficient 159.69508928 because B declines a later experiment with negative own gain. Adding the R1 marginal-only priority toll .6405 to the claim route does not change the equilibrium. This computation exposes both initial free-riding and a supported continuation underresearch boundary.

## D.5 Signed continuation incentive and full payoff alignment

At a last-slot history with only i's experiment available, the joint gain is b_i+a_j|i^+. At a nonnegative fee the active owner will not undertake an experiment with nonpositive own b_i. If the sum is positive despite that, no such fee implements. A conditional credit equal to a_j|i^+ makes the owner's gain equal to the joint comparison. A strict credit above -b_i is required for strict research if b_i<0, with equality permitting the prescribed action tie. This proves Theorem 6's exact boundary.

This final-slot credit is not enough to certify the root equilibrium. A's release-and-free-learn payoff and B's retention responses can also change. The full finite-game solution above must be recomputed under any proposed transfer scheme, including future credits. The paper does not claim that the last-slot credit alone attains the optimal root value.

For the stronger theoretical team-payoff contract, let realized resource payoffs, including all own costs and terminal reward, be X_A and X_B. Give i a signed additional internal transfer X_j-K_i, where K_i is an initial fixed constant independent of subsequent choices and signals. Its private total becomes X_A+X_B-K_i. At every public decision, maximizing conditional expected private payoff is maximizing the same total resource value. The finite game's backward induction then selects the joint-optimal feasible continuation at every history, and hence (9)-(11). All eight root choices and all final retention plans are attainable through the defined sequential moves, so no central-feasible action is excluded by the priority right when both owners share this objective.

This is an elementary sufficient alignment result, not a new private-type mechanism. Transfers may be positive or negative, need not balance within owners, and require observable eventual payoffs and authority over internal marginal incentives. Adding both transfers to social payoff would be wrong: the firm objective is still X_A+X_B, not twice that quantity. A fixed constant changes distribution, not decisions. These assumptions are stronger than those of the restricted one-time priority fee, and the construction is not asserted to satisfy the published dynamic-pivot participation or truthfulness conditions under correlated private information.

## D.6 Exact example and independent enumeration

For mu=(.58,.02,.02,.38), q_A=.8, q_B=.95, c_A=1, c_B=30, h_A=h_B=.01, S_A=S_B=100, and zero d and r, all state and relevant signal branches have positive probability. Conditional on A surviving, its signal is 1 with probability 11/25 and 0 with probability 14/25. After signal 1 the posterior is (29/110,1/110,2/55,38/55). After signal 0 it is (29/35,1/35,1/140,19/140).

If both survive and the first signal is 1, the final research plan keeps both unresolved and researches B. At this posterior, g_A=800/11, g_B=70. B's own gain is -119/20, while A's cross-information gain is 9401/550. The total increment is 12257/1100. Expected final case payoffs are 4491/50 for A and 1281/20 for B, totaling 15387/100. With a first signal 0, both act for a total 1185/7. These values include the final-slot costs and hazards.

The six first-slot branches have probabilities 1/10000 (neither alive), 99/10000 (only B alive, no delivered A signal), 693/125000 (only A alive, signal 0), 1089/250000 (only A alive, signal 1), 68607/125000 (both alive, signal 0), and 107811/250000 (both alive, signal 1). They sum to one. Weighting the final values and subtracting first-slot acquisition/holding costs gives 249523577/1562500 exactly. The root comparison with every other retained-set/active choice is supplied in JSON and the main table.

The independent enumerator pre-draws physical latent states, both potential signals, and both survival coins per case. It evaluates actual terminal correctness on each path, using a separately calculated likelihood-based action at the information available when that action is locked. The evaluator does not call the rational final-slot formula or root solver. It enumerates all root actions and all observable-history contingent final plans, including retention of the already researched case. Final idle plans are excluded only by the analytic dominance proof; root idle plans are enumerated.

For positive-probability interior branches the number of final schedule/retention maps per root action, in order empty, idle A, active A alone, idle B, active B alone, idle both, active A with both, active B with both, is 1,2,1,2,1,20,18,18, totaling 63. For idle both, both-live states allow five plans (stop; A active with B stopped or retained; B active with A stopped or retained), each singleton survivor allows two, giving 5*2*2=20. For active A with both retained, each both-live signal node allows three plans and the B-only survivor node allows two, giving 3*3*2=18. Other nodes have no remaining experiment or no case. Branches of zero probability reduce counts. Bayes-optimal terminal actions are imposed, not counted as distinct deliberately mistaken policies.

There are exactly three named checks, with 63,30,63 maps, totaling 156 output rows. They are the full-support correlated example, a perfect-correlation zero-expiry boundary, and the product prior with the same marginal probabilities and other primitives. Both all-root comparisons and implementation boundary checks are executed, 37 in total. This is a finite exact calculation and enumeration, not a Monte Carlo simulation or a larger queue study.

\newpage

# Appendix E. Two-credit implementation: exact regional proof

## E.1 Fixed institution, no omitted payments

This appendix proves Theorems 7-8 on I=[17/100,23/100]. It retains Appendix D's latent binary states, public signal histories, independent .01 expiration, one experiment per case, local priority rights, and immediate-action options. C is earned by conducting initial A research, not by retaining both or by successful survival. B's credit requires that A was initially researched, both survived the first slot, A's delivered signal was 1, and B conducts its final experiment. The payment is earned before its second survival coin. No credits arise after initial B research, initial idling, or terminal action. Credits are sunk once earned and do not change subsequent terminal-action preferences. No experiment can be repeated to collect another credit.

The zero-own-gain research/action tie selects action. A positive initial claim/release tie selects its priority claim, consistently with the original local institution. These are different ties. Conditional Bayes-action ties can use action 1 without affecting expected payoffs. Weak implementation means the outcome chosen by these conventions; strict supported implementation means strict root and discretionary on-path research/retention incentives. It does not require every unused off-path option to have a strict ranking.

## E.2 Joint policy and complete exact interval certificate

Write s=99/100 and h=1/100. The target policy has the fixed research/retention decisions in Section 8.4. Terminal actions are also fixed on I: if only A survives its first experiment, act according to that signal; after both survive signal 0, both choose action 0; after both survive signal 1 and B is studied, both surviving cases choose B's signal, except that A uses its initial signal if B expires and no second signal arrives. If A expires initially, B's one experiment uses the prior and its own signal. All these terminal choices are Bayes optimal throughout I. This follows by comparing the unnormalized masses of each binary state after each observed signal. The only two-signal Bayes-action switch inside I is at 41/225 for A after (Y_A,Y_B)=(0,1), a signal pair the target policy never generates because it stops after Y_A=0.

The target's fixed physical resource components can be derived without posterior division. The relevant joint probabilities are

$$\Pr(\theta_A=0,Y_A=0)=.48,\quad
\Pr(\theta_A=1,Y_A=1)=.32,$$
$$\Pr(Y_A=1,Y_B=\theta_A)=.202+.9\delta,\quad
\Pr(\theta_B=0,Y_A=0)=.336+.6\delta.$$

Consequently

$$X_A=-1+100\{sh(.8)+s^2(.48)+s^3h(.32)
+s^4(.202+.9\delta)\},$$
$$X_B=sh(64.05)+100s^2(.336+.6\delta)
+s^2(.44)(64.05). \tag{E1}$$

The A cost is paid once even if it expires. B's research payoff 64.05 already includes its final acquisition cost 30 and survival-weighted reward .99(95). The B-only branch uses that value, while the both-surviving signal-1 branch has probability s^2(.44). Thus neither cost nor lost opportunity is counted twice. Expanding (E1) gives (14), so the target value is affine in delta.

For completeness, the maximum physical payoff at every root choice is certified exactly at both interval endpoints:

| Retained set, initial assignment | delta=17/100 | delta=23/100 |
|:--|--:|--:|
| Neither, none | 120 | 120 |
| A only, idle | 68709/500 | 68709/500 |
| A only, A | 691/5 | 691/5 |
| B only, idle | 246819/2000 | 246819/2000 |
| B only, B | 2481/20 | 2481/20 |
| Both, idle | 36853237179/250000000 | 38582309997/250000000 |
| Both, A | 30486421447/200000000 | 161147685689/1000000000 |
| Both, B | 729696081/5000000 | 312339/2000 |

These fractions are finite sums over latent states, potential binary signals and the four potential independent survival coins. At each root the evaluator enumerates every final schedule/retention map, with terminal Bayes actions evaluated separately from the joint solver. There are 63 maps per prior. At both endpoints and the witness, the target is the unique maximizing map; the closest distinct map is lower by 8019/200000=.040095. This is the loss from omitting the worthwhile B-only continuation on its positive-probability survival branch.

To prove the continuum, fix any feasible pure physical policy, including its terminal actions. Its expected payoff is affine in delta because the joint prior is affine and signal/survival likelihoods are fixed. The maximum over terminal actions or any collection of policies is therefore convex. For any competing root choice, its optimized payoff is convex, while the target payoff (E1) is affine. The target strictly exceeds it at both endpoints by the table, hence strictly exceeds it throughout the closed interval by the defining convexity inequality. The same reasoning compares every distinct final schedule/retention map under the target root: its terminal-action-optimized value is convex, and the target exceeds each at both endpoints. This proves strict optimality of the target map on I. No extrapolation from a sampled grid or unproved monotonicity is used. Appendix D's final-idle dominance removes only decisions that cannot improve a payoff; root idle choices are explicitly included.

## E.3 All final-slot local continuations

After initial A research and survival of both cases:

1. If Y_A=1, B's own uncredited research gain is -K. Its gain including the observable-history credit is kappa-K. The zero-gain tie selects action, so research occurs exactly when kappa>K. A's passive cross-information gain is (4410450 delta-594259)/22000, strictly positive on I, and it strictly retains if research occurs. Otherwise both act. Joint research is strictly valuable because the sum is (1410450 delta-65159)/22000>0.
2. If Y_A=0, B's own gain is -3(5000 delta-189)/140<0 and no credit is eligible. Thus it acts, and A acts as well. A's hypothetical benefit from a B experiment cannot itself make B conduct it.

If A expires but B survives, expiry is uninformative and B researches at gain 81/20. If only A survives, no experiment remains and it acts using its delivered signal. If neither survives, there is no choice or further payoff. All six positive-probability first-slot histories are thereby covered. Payment C was already earned and is irrelevant to all these continuations.

Off the target route, after initial B research, no credit is ever eligible. If both survive B's signal 0, A's own research gain is -2(225 delta+236)/295<0, and both act. After B's signal 1, A researches exactly when delta<delta_0. On this profitable branch its own gain is (7831-45000 delta)/205, and B acts before the experiment because its passive gain is -38/41. At delta_0 A's zero gain selects action. For delta>delta_0 research remains unprofitable; beyond 41/225 the uncredited own gain has the expression -(450 delta+287)/205, also strictly negative. B's passive cross gain after its signal 0 is -57/59. If B expires and A survives, A researches with uncredited gain 91/5. If only B survives its own first experiment, it acts. These are all B-first survival/signal continuations.

After initial idle retention of both cases, both experiments remain. If both survive, A's own immediate research gain is 91/5, whereas releasing to B gives A the larger cross gain

$$a_{A|B}(\mu)=\frac{99^2}{100^2}100[(.518+1.8\delta)-.6]-.6>91/5.$$

The inequality holds at 17/100 and increases thereafter. B's own gain is 81/20>0, so A releases, B researches and A retains. The own/passive components are precisely those of the local game, not the joint-optimal final assignment. If only A or B survives, that case conducts its own profitable experiment. With a single case retained initially, the same singleton continuation applies; a case researched initially cannot repeat research. With no live cases, nothing occurs. This exhausts initial-idle, singleton and empty-root continuations as well as both research roots.

For transparency about unused ties: the Bayes-action tie at 41/225 is on an unchosen two-signal route; A's hypothetical retention tie after initial Y_A=0 and a subsequently conducted B experiment is at delta=137947/735075, because the cross gain above 41/225 is 3(735075 delta-137947)/14000. B never chooses that uncredited experiment on I. Neither tie changes (17) or funding. A stronger requirement that every conceivable off-path action and terminal Bayes choice be strict would fail at these points and at delta_0 without further instruments. The stated strict supported implementation deliberately does not claim that stronger property.

## E.4 Root follower choices, including failed-continuation credits

If A initially claims, B can act for 60 or retain. Let

$$Y_B^0=50.815215+117.612\delta.$$

This is its resource/private payoff from retention if it does not conduct research on the both-live signal-1 branch. It includes the uncredited B-only experiment after A expires. It is strictly above 60 throughout I. If kappa>K, its retained private payoff is $X_B+p\kappa=Y_B^0+p(\kappa-K)>60$. If kappa<=K, no eligible experiment occurs and the retained payoff is Y_B^0>60. Thus B strictly retains for **every** pair of nonnegative instruments, not only after imposing the target policy. This also proves the retention slack at the witness's limiting credit.

If A releases but stays unresolved, B may (i) act immediately, leaving only A to wait, (ii) conduct its experiment with both retained, or (iii) wait with A. Its respective own payoffs are

$$60,\qquad64.05,\qquad .99(64.05)=63.4095.$$

The third value follows from the actual no-signal final local game just derived, including the cases in which A expires first. It is not inferred from a centrally imposed continuation. B strictly chooses (ii). If A acts and releases, B has exactly the same own three values and again researches initially. These comparisons fully resolve the follower sets C,R,X of Section 8.2, including idle and immediate-action alternatives.

A's private payoffs for claim, release-and-retain, and act-and-release are therefore

$$\begin{cases}(X_A+C,R_A,60),&\kappa>K,\\
(78.2+C,R_A,60),&0\leq\kappa\leq K.
\end{cases} \tag{E2}$$

The second branch exists only when K is nonnegative. Without the later B experiment, A's research payoff is .99(80)-1=78.2. In both branches B's root retention is optimal. Since R_A>60 and R_A>78.2 on I, the actual local equilibrium is A-first exactly when C is at least R_A minus its corresponding research component in (E2); otherwise it releases and waits. A's act-and-release option is feasible but strictly dominated by release-and-retain here. This solves root behavior also for instrument pairs that fail implementation.

To derive R_A, if B expires initially and A survives, A researches for 78.2. If both survive, without A's further experiment it acts according to B's signal, whose unconditional correctness probability is .518+1.8 delta. After B's signal 1, its possible own profitable research adds the positive part derived above. Hence

$$R_A=sh(78.2)+100s^2(.518+1.8\delta)
+s^2(.41)[(7831-45000\delta)/205]^+,$$

which is (18). Subtracting (E1) yields the two pieces (16). The low piece has positive intercept and slope; the high piece is increasing and agrees with the low piece at delta_0. F is positive everywhere on I. Combining (E2) with B's strict research condition proves both directions of (17), not merely a sufficient deviation check. Once the continuation is induced, kappa has no further effect on A's resource component, so even an arbitrarily large continuation credit cannot replace C. A nonnegative initial toll makes its strict free-riding preference stronger.

## E.5 Funding constraints and endpoint interpretation

The payment random variable on the implemented policy is $C+\kappa\mathbf1_{\mathcal H}$, where $\Pr(\mathcal H)=p=s^2(.44)>0$. The event is research after the first signal-1/both-survive history; it does not require either second-slot survival. Both events of receiving C alone and of receiving C+kappa have positive probability. Thus (19) is exact, including the payment after initial A expiry. No eventual realized reward need be observed for settlement.

Put $k=K^+$. The implementation set is the product of C>=F and the half-line kappa>=0,kappa>K; for strict supported implementation replace the first inequality by C>F. Consequently the weak expected/pathwise infimum functions are piecewise F below delta_1 and F+pK/F+K at or above delta_1, with F itself changing slope at delta_0. At delta_0 the two F formulas coincide; kappa=0 is feasible because K<0. At delta_1, kappa=0 fails by the zero-gain action tie, so the continuous infimum ceases to be attained. At both closed endpoints of I the respective formulas and tie conventions apply without taking an unstated open neighborhood. No claim is made just outside I or at independence, where the target pattern need not persist.

For weak implementation, a single cap equal to its infimum is feasible exactly when delta<delta_1. For strict supported implementation no equality cap is feasible anywhere on I. Under simultaneous expected/pathwise caps, both corresponding slack or weak inequalities are required. Sufficiency follows by choosing sufficiently small increments in each payment, rather than treating an expected limit as permission to exceed a pathwise limit. Since both outlays are increasing in C and kappa, there is no unaccounted trade-off permitting a smaller initial payment in exchange for a larger continuation payment after the efficient branch is induced. These are gross funding requirements for this specified class, not firm resource costs or minimum funding over all possible mechanisms.
