---
title: 'Paper 10 R3: Prospective Shared-Analyst Queue Experiment'
date: '17 October 2026 | Proposed, not registered or implemented'
geometry: margin=1in
---

# P.1 Status, unit, and estimands before methods

No partner, data agreement, approved treatment, recruitment, observations, or experiments exist. This is a prospective protocol. The theoretical model has two one-experiment cases and two slots, with independent and correlated binary-state specifications. The study tests its shared-capacity mechanism in eligible operational queues, not its literal numerical calibration.

Primary unit: an analyst-queue episode with a frozen intake cohort and a defined capacity window. A queue consists of all cases sharing the same analyst/reviewer resource. An episode can contain more than two cases; theoretical optimality is not asserted for that larger queue. A matched two-case substudy is possible only if the institution can document a bounded two-slot decision window and reserve capacity without displacing uncounted cases. Cases excluded from the cohort but affected by reserved capacity must be followed as spillovers.

Primary estimand: intention-to-treat effect of offering an opportunity-loss scheduling aid on total 90-day net payoff summed over the episode's registered cases, averaged equally across a crossed evidence-provision assignment. The primary target is the mean episode total at the prespecified cohort definition, not a mean among completed purchases. Report case-weighted results secondarily. Unequal episode size and any weighting are frozen before assignment.

If defensible monetary bounds are incomplete, the primary estimand is interval valued. Declare a favorable welfare effect only when its lower confidence bound is positive across the prespecified admissible valuation set. A faster queue with worse total expected payoff is not a successful treatment.

Secondary confirmatory family, with Holm adjustment across seven contrasts: evidence provision effect on total payoff; aid-by-evidence interaction on total payoff; aid effect on all-worker analysis minutes; aid effect on summed unresolved case-hours through day 90; aid effect on cases completed by day 30; aid effect on expired cases; aid effect on total rework and switching expenditure through day 90. Case reversal rates and mechanism interactions are exploratory and explicitly labeled.

# P.2 Feasibility and eligibility

Seek a partner with routine, non-safety-critical procurement decisions, reliable intake for purchases and rejections, logged evidence requests, a shared analyst roster, verified quote expiry, and linked operational outcomes. Exclude safety-critical, legally mandated, personnel, emergency, and strategic high-value reviews. The partner defines exposure caps, authority limits, and reversible-action terms before enrollment. No such caps are invented here.

A read-only feasibility audit must establish: the actual shared-resource boundary; how managers currently claim priority; whether immediate action really avoids analyst use; packet production durations; existing mandatory reviews; rejected/unresolved intake coverage; capacity window commitments; and spillovers to adjacent queues. If terminal approval itself uses the same scarce reviewer, the two-slot research-only model does not fit without redesign. Record that mismatch rather than silently treating both services as the same.

Public BPI Challenge 2019 organizer documentation verifies a procurement-process event-log candidate. Repository/file access and license were not verified; no schema or rows were analyzed. It lacks a verified research-queue mapping in this work. It may inform process measurement if later accessed under its actual terms, but cannot identify the treatment effect without intake, resource links, and economic outcomes.

# P.3 Design and treatments

Use a parallel 2-by-2 design at the whole independent analyst-pool level. If too few pools exist, consider randomly assigned pool-period blocks only after demonstrating feasible washout and tracking all carryover cases; this changes assumptions and requires a new registration. Do not randomize individual cases independently in one shared queue and then assume no interference.

Evidence factor: provide one frozen incremental packet for each eligible case, versus existing information. Packet production time, source costs, and worker effort count in the resource ledger. Keep purchasing alternatives, legal information, price opportunities, and formal authority comparable. Display design is held constant conditional on provided facts. A compressed-display substudy, if later chosen, must preserve accessible content and has an attention estimand rather than an acquisition estimand.

Scheduling factor: offer a queue-level opportunity-loss aid versus existing priority practice. At a review point, the aid records for each case: current best action; available incremental experiment; credible expected action improvement; acquisition time; option to act immediately; consequences of waiting; quote expiry; recoverability; and the identity of other cases displaced by the next analyst slot. It distinguishes a research value estimate from a deferral-loss estimate. It displays a proposed research order and explicit act-now or retain-for-later decisions, with documented overrides.

Record prespecified cross-case prior links, signal-source identities, posterior revisions in both cases, and whether an already researched case remains unresolved to receive another case's signal. Do not infer independence merely from separate case records. Correlated episodes require a joint prior and signal model; applying the independent u-score to updated marginals is not justified. The final-slot information credit is a theoretical incentive calculation, not an authorized transfer treatment.

In verified independent two-case one-packet episodes, the aid can calculate b, w, and u under transparent parameter inputs. In larger queues it is only a documented scheduling recommendation, not a theorem-backed globally optimal index. Uncertain inputs must produce sensitivity ranges, not a falsely precise rank. Record when ranks are indeterminate over the full uncertainty set.

The offered aid does not implement real marginal incentives automatically. No effect is labeled a toll-mechanism treatment effect. If management later authorizes actual internal charges, register a distinct arm specifying who pays, when, whether later service is uncharged, whether the charge changes the marginal budget, and whether the analyst's priority right is enforceable. A generic charge per minute is not the posted first-slot charge in Theorem 3. No actual charge, binding deadline, or authorization change is part of the present study.

# P.4 Interference and identification

Treatment directly changes delay on other cases; that spillover is the mechanism. The primary total episode payoff includes it. Randomization identifies the policy-offer effect if cohort registration is unaffected by assignment, outcomes are measured comparably, and cross-pool spillovers or carryover are either negligible or included in a prespecified exposure design.

Use staffing and resource rosters to identify shared analysts, reviewers, vendors, stock constraints, and work redirected outside the pool. Log both treated and displaced cases, including unserved requests. Estimate exploratory effects by exposure to treated competing cases, but do not call those causal direct effects without a registered interference model. If resource sharing is organization-wide, the independent-pool design may be infeasible. The correct response is redesign, not inflated apparent sample size.

Analyze with a saturated factorial regression or assignment-based contrast at episode level, retaining randomization strata and frozen baseline load, case mix, and holding exposure covariates. If episodes repeat within pools, inference clusters at the assignment pool. Use randomization inference consistent with the actual assignment, with small-cluster robust inference as a companion. Define the aid main contrast as equally averaged across the two evidence levels.

Do not control in the main regression for post-treatment completed-case status, evidence requested/opened, research minutes, priority rank, or elapsed time. These are mediators/outcomes. Pre-treatment difficulty measures include novelty, baseline available evidence, stakes, number of alternatives, resource requirement, approval layers, and time sensitivity.

The mechanism prediction is that changing priority rights or accounting for a rival's deferral loss matters most when local and joint orderings disagree. Define disagreement using frozen pre-treatment inputs and a documented valuation uncertainty set. Larger effects in queues with split budgets or severe load are descriptive heterogeneity unless those features are randomly manipulated. A future randomized display of verified competing-case costs could sharpen a mechanism test while holding the focal packet fixed.

# P.5 Data dictionary and timing

| Variable | Definition and units | Source/timing | Main concern |
|:--|:--|:--|:--|
| pool_id | All cases sharing analyst capacity | Baseline roster | Hidden shared workers |
| episode_id | Frozen cohort and capacity window | Intake before assignment | Selective episode construction |
| case_id | Unique decision, bundled lines resolved | Intake | Split/duplicate cases |
| eligible | Pre-treatment inclusion rule | Intake attributes | Strategic exclusions |
| assigned_E, assigned_S | Evidence/aid assignments | Randomization ledger | Offer versus uptake |
| competing_ids | Cases displaced by a requested slot | Resource ledger | Unrecorded opportunity loss |
| priority_owner | Existing first-slot right and override authority | Baseline process | Informal authority |
| analyst_available | Research capacity by slot and worker | Staffing log | Capacity altered by treatment |
| request_time | First research/decision intake | System log | Backdating |
| research_start_end | Work on each experiment | Work log/time sample | Offline work |
| passive_exposure | Unresolved waiting time without own research | Derived log | Calendar time versus active effort |
| action_time_type | Purchase, reject, expire, or unresolved | Authorization/terms | Missing rejections |
| expiry_time_terms | Verified quote/opportunity expiry and extension | Vendor terms | Endogenous extension |
| prior_risk | Frozen uncertainty assessment | Pre-treatment rubric | Unvalidated probabilities |
| packet_quality | Likelihood/precision evidence where estimable | External historical validation | Availability not use |
| stakes_recovery | Documented action loss and recoverable share/cost | Baseline contracts | Recovery treated as free |
| all_worker_minutes | Focal and displaced workers' active time | Linked work sampling | Unobserved displacement |
| terminal_net_value | Realized action margin before other exclusive costs | Finance/operations | Missing unchosen outcome |
| rework_switching | Downstream corrections, reversal and replacement cost | 90-day follow-up | Delayed posting |
| residual_holding | Cost schedule not counted in margins/expiration | Independent costing | Double counting |
| cost_bounds | Justified lower/upper costs and dependencies | Before outcomes | Favorable valuation selection |
| unresolved_90 | Registered case still open at day 90 | Follow-up | Completer selection |
| episode_bounds | Sum of all case and resource payoff bounds | Derived ledger | Omitted cases and external work |

This is a proposed schema, not verified columns from a firm dataset. Independent validation is needed before treating stated confidence as a calibrated prior or a packet's quality as a likelihood. Data availability, precision, actual evidence use, capacity rights, and outcomes are distinct variables.

# P.6 Welfare ledger, missing outcomes, and bounded costs

Each resource cost and consequence has one ledger category. Acquisition expense counts actual production and analyst work once. Holding exposure counts residual lost capacity or operating costs not already counted in action margin or expiration losses. Expired cases have no realized opportunity payoff under the literal model, but real organizations may retain salvage; the field ledger must use verified institutional terms instead. Transfers for hypothetical internal priority charges are excluded from organization-wide payoff.

The theoretical externality u_j is not added to observed downstream loss. It is an opportunity-cost comparison used to schedule; realized policy payoff already includes the rival case. Adding both would double count. Likewise, a nominal time saving is not necessarily cash savings; report physical minutes and scarce-capacity shadow-price bounds separately.

At a fixed implemented policy, mean payoff is evaluated for all enrolled cases over the same horizon. Random assignment identifies total realized policy value without observing every unchosen supplier's quality. It does not identify decision-specific regret relative to an oracle. Common independent ex post market information may support a secondary quality measure only under a validated mapping to economic outcomes.

Report unresolved and missing-payoff fractions by arm. Never compare mean delay only among completed cases. Sum restricted case-hours through the fixed horizon, with explicit rejection treated as resolution and expiration as a competing event. If missing case payoff is institutionally bounded by [L_i,U_i], use those bounds. Without defensible limits, do not assign zero or simulate informative losses. Report worst-case mean contrasts and sensitivity to missingness. MAR imputation may be secondary only with assumptions stated.

For fixed policy z and known non-delay primitives, uncertain residual costs give $W_z=A_z-\sum_i d_iT_{iz}$. Endpoint bounds hold that policy and the full signal/reward/expiration model fixed. They do not establish robustness to model error. With uncertain priors, recovery, precision, or hazards, define a full joint uncertainty set with documented dependencies and recompute every candidate policy contrast. Require uniform nonnegative lower comparison for a certified ordering; otherwise report ambiguity. No such real-data uncertainty set is currently estimated.

# P.7 Precision and feasibility planning

Illustrative arithmetic only: with 120 genuinely independent analyst pools, 20 episodes per pool, balanced four-cell assignment, and episode-payoff ICC .05, the design effect is 1+19(.05)=1.95. The normal-approximation 80% power, two-sided 5% aid-main-effect MDE is $(1.96+.84)\sqrt{4(1.95)/2400}=.160$ episode-payoff standard deviations. The corresponding factorial interaction MDE is .319 SD. At ICC 0 and .10, main-effect MDEs are .114 and .195 SD. These are hypothetical pools and episodes, not observed sample sizes, variances, or power estimates.

The independent assignment unit must be real. Twenty cases in one episode are not twenty independent queue experiments, and repeated episodes with the same analyst require clustered inference. Unequal episodes, fewer pools, carryover, uptake failures, and wide payoff bounds worsen precision. Final power requires a partner's baseline outcome variance, ICC, assignment structure, and economically meaningful currency or capacity effect, followed by simulation under the actual design. None is available.

A feasibility pilot measures only nuisance quantities and operational limits, not a treatment-effect-driven outcome choice. Freeze final enrollment, cohort rules, hypotheses, valuation bounds, and analysis dates before examining treatment outcomes. No unadjusted repeated p-value peeking is planned. Any confirmatory interim analysis requires a separately registered alpha-spending or always-valid method.

Go/no-go gates: complete intake; real independent capacity pools; auditable priority rights; comparable alternatives and capacity; bounded stakes; linked all-case outcomes; displaced-work coverage; and institutional authorization. Failure triggers redesign rather than a nominal larger N.

# P.8 Unpopulated reporting template

| Assignment | Registered episodes | All cases | Unresolved fraction | Total minutes | Payoff lower/upper |
|:--|:--|:--|:--|:--|:--|
| Standard packet, local order | Not observed | Not observed | Not observed | Not observed | Not observed |
| Added packet, local order | Not observed | Not observed | Not observed | Not observed | Not observed |
| Standard packet, queue aid | Not observed | Not observed | Not observed | Not observed | Not observed |
| Added packet, queue aid | Not observed | Not observed | Not observed | Not observed | Not observed |

No empirical estimates, assignments, p-values, or implemented organizational outcomes are supplied. Synthetic model results belong to the theory section only.

The two-credit result is theoretical only. A future feasibility audit could distinguish expected internal credit authorization from gross pathwise funding capacity and verify that research and the specified public signal history are observable. It supplies no authorization to pay credits or add an experimental treatment, and no real transfer data exist.
