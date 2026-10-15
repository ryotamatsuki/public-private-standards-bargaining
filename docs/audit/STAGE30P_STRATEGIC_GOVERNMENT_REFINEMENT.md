# Stage30P — Strategic government policy implementation and limits

2026-10-15 JST. Audit of strategic governments, *not* a paper rewrite or claim of unrestricted-vote SPE.

## Original problem

Stage30C C1–C7 and Stage30N use a prescribed national policy selector. Let initial firm history be h and government national-welfare difference be Delta_i(h)=W_i(M|h)-W_i(L|h). The original selector mandates M iff

    |S(h)| >= r AND A intersect S(h) is nonempty,
    S(h)={i: Delta_i(h)>=0}.

Under unrestricted simultaneous r=2 binary voting, all-NO ballots are Nash even if every country strictly gains from M, because a sole YES cannot pass. The original selector cannot be asserted as all government Nash play.

We preserve all original corporate/market primitives, firm N/O(c,a) continuum, sunk K, public O(1,0), national profit plus domestic CS, strict compliance after M, no transfers, and C1–C7 baseline eta/K rectangle. We change only the POLITICAL extensive form as follows.

## Fully specified, strategic sequential government protocol

The constitution announces a fixed nonempty proposer set A, quota r in {1,2,3}, proposer turn order and voter roll-call order, all before private investment. At any date-2 firm history, eligible governments choose sequentially whether to offer the *fixed* public mandate M. An offer immediately triggers a binding sequentially observed YES/NO vote of all three governments. The first referendum settles policy; absent any offer policy L remains. Motion and vote have zero direct procedural costs. Successful M brings the original compliance and Cournot payoffs.

Country i evaluates all continuation actions using its actual material Delta_i(h). At exactly Delta_i(h)=0 **only**, it lexicographically prefers policy M to L. This is the original YES-on-tie selection represented as an explicit preference refinement; it is NOT implied by being materially indifferent. Nonpivotal actions need not be sincere.

## Proposition P1 — all pure sequential-government SPE policy OUTCOMES

For **every** real Delta vector, every initial investment history h, every nonempty A, r in {1,2,3}, and any ex ante fixed proposer/voter orders, the sequential political game admits pure SPE and ALL its pure SPE have the same terminal policy:

    M iff at least r governments have Delta_i>=0
         AND at least one such government belongs to A.

All government strategy profiles and individual ballots need not be unique.

### Proof

Backward induction over the roll-call vote. At an intermediate node let y be prior YES ballots and let p be remaining voters preferring M (including lexical-zero types). If y+p<r, the remaining opponents can prevent M and every pivotal opponent strictly chooses NO, so all continuation SPE yield L. If y+p>=r, the remaining proponents can meet the quota and every pivotal proponent strictly chooses YES, so all continuation SPE yield M. The induction covers arbitrary roll-call order and nonpivotal action indifference. At its root the referendum therefore succeeds iff |S|>=r.

If the referendum cannot pass, no offer can change L. If it can pass, backward induction over proposer turns yields M exactly when some remaining eligible government weakly prefers M in material payoffs (lexically prefers M when tied): the last such proposer can force M, each earlier proponent can force or rely on a later proponent, and an opponent never proposes a harmful M if doing so would change the outcome. The exact terminal policy is independent of proposer order. QED.

This is only a binary known-payoff political game; it is NOT an agenda theorem for alternative policy contents, vote trading, asymmetric information, or tactical misrepresentation over multiple issues.

## Proposition P2 — preserve original all-real corporate C1–C7 under sequential politics

For the unchanged Stage30C parameter rectangle and original firms' action spaces, replacing the **prescribed** political selector with this explicitly sequential political game leaves the entire initial pure-firm SPE correspondence and terminal payoffs of C1–C7 unchanged for each fixed A,r.

Reason: P1 selects exactly the same L/M outcome **after every possible firm investment vector h**, including off-path unilateral deviations and tie histories. Since adoption/compliance, Cournot and investment costs also remain identical, each firm's payoff under each first-stage profile is identical to its source Stage30C payoff. The full initial-game best-response problem is the same, and the previous all-real proof transfers. This is a *payoff equivalence theorem conditional on P1*, not a fresh independent Cournot or investment certificate.

Stage30N follows with fixed r=2 and fixed country labels: old A={3} allows O(c,a),O(c,a),N private SPE when (c,a) belongs to R={F_a>=0,F>=P,K>V}; new A={1,3} eliminates all private-terminal pure SPE while leaving public outcomes. C4 set expansion, C2/C5/C6 welfare support and C7 national incidence transfer as well.

No claim that the 7D Stage25 **whole** box supports C1–C7; that source only gives partial scope.

## Exhaustive finite policy-game audit

Source: code/stage30p_sequential_voting_spe.py.

Enumerates 3^3=27 ordinal government sign/tie profiles, all seven nonempty proposer sets, three quorums, six voter permutations, and every ordering of eligible proposers. Since binary policy preferences depend only on sign and lexical equality, this spans *all* real Delta preference configurations for government choices.

Result of independent Python backward induction: **486 referendum subgames and 7,290 motion-plus-referendum subgames**; every computed pure SPE terminal policy equals the original selector. Explicit fixed-quorum (+,+,-) test: A={3} yields L at r2; A={1,3} yields M at r2; r3 yields L. The finite evaluator includes every continuation outcome under nonpivotal action ties; it does not assume a sincere ballot path.

Exact-tie negative control: Delta=(0,-,-), r=1, A={1}, no lexical M tie preference => both policy terminal outcomes are possible; lexicographic tie convention => only M. Hence P1 would be FALSE without its explicitly stated tie refinement.

## Stronger negative control — unrestricted simultaneous voting can destroy C3

In a simultaneous costless referendum r=2, a profile with all three ballots NO is Nash whatever the material government gains: changing one ballot to YES cannot enact M. Apply this as the government voting continuation after *every* possible investment history; let all eligible governments abstain from proposing (an individual offer is useless if the recorded all-NO continuation persists). Government play is sequentially rational within that simultaneous referendum protocol at every history.

Take initial firms N,N,N. Public M never happens; under L a unilateral O(c,a) firm has no matching open counterpart, so demand is unchanged and it loses the strictly positive cost K+phi(c²+a²)/2. Thus **NNN followed by L is a pure SPE** of this unrefined simultaneous-political extensive form, even under r=2 with two eligible proposers. This directly disproves C3 if it is advertised as an unrestricted six-player strategic-government result.

A separate r=1 simultaneous-AGENDA concern: if one country favors M but lacks proposal rights and two opposing eligible governments both table M, neither opponent may unilaterally stop passage because the other continues to propose. The sequential-motion design prevents this redundant-proposal Nash phenomenon. Changing only the voting order without resolving agenda coordination would be incomplete.

## Editorial significance and unresolved limits

**A concrete strategically founded policy institution does preserve both main full-paper contributions.** P1 shows how government behavior can be entirely strategic with complete-information moves rather than a prescribed sincere action rule. P2 links this to the old C1/C3 and C5/C6 theorems by an every-history policy payoff bridge.

**Do NOT write:** all simultaneous government Nash SPEs produce M under broad agenda, or that this is a general mechanism design novelty. The sequential protocol is a separately specified institution, not a theorem about the original unrefined voting game. The exact zero-payoff tie convention remains an explicit selection device.

The categorical N versus O(0,0) demand shift, nonzero government mandate-cost failure case, and four full published-priority studies remain unresolved. A policy-implementation derivation improves one central referee objection but by itself does NOT authorize submission, paper freeze, or a broad welfare-policy recommendation.

Related voting theory: Kleiner and Moldovanu (2017, AER) sequential voting and content-based agendas; Spenkuch, Montagnes and Magleby (2018, AER) sequential roll-call behavior; and binary referendum incentives (JAERE 2014). These are methodological precedents, not evidence of novelty for P1.

**Status:** government strategic implementation scoped PASS for the new *sequential* protocol; all original unrestricted strategic Nash claims remain NO-GO. Stage30M editorial submission NO-GO and Stage7.5/priority gates unchanged.
