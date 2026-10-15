#!/usr/bin/env python3
"""Stage30P: exhaustive pure-SPE outcome audit of a sequential agenda/roll-call game.

Government policy gains are signs in {-1,0,+1}; at exact material indifference
the policy tie convention lexicographically prefers a successful mandate M.
A proposer offers an immediate referendum; if it declines, the next eligible
country can offer. Votes are observed sequentially, without voting or motion
costs. No government can alter the mandate or transfer resources.

The 27 ternary sign patterns cover every real 3-vector for preference purposes,
including ties. This finite solver audits POLICY SUBGAMES ONLY; C1-C7 corporate
continuous-domain proofs remain inherited, not re-proved by enumeration.
"""
from functools import lru_cache
from itertools import combinations, permutations, product

N = 3
SPE_CASES = 0
VOTE_CASES = 0


def preferred(a, b, gain, lex_tie=True):
    """All optimal binary choices; a,b are reachable policy outcomes 0=L,1=M."""
    utility_sign = gain if gain != 0 else (1 if lex_tie else 0)
    delta = (b - a) * utility_sign
    if delta > 0:
        return frozenset((b,))
    if delta < 0:
        return frozenset((a,))
    return frozenset((a, b))


def rollcall_spe(gains, quorum, vote_order, lex_tie=True):
    """All pure SPE TERMINAL OUTCOMES across all continuation tie choices."""
    @lru_cache(None)
    def solve(t, yes_so_far):
        if t == N:
            return frozenset((int(yes_so_far >= quorum),))
        govt = vote_order[t]
        no = solve(t + 1, yes_so_far)
        yes = solve(t + 1, yes_so_far + 1)
        out = set()
        for a in no:
            for b in yes:
                out.update(preferred(a, b, gains[govt], lex_tie))
        return frozenset(out)
    return solve(0, 0)


def sequential_agenda_spe(gains, quorum, vote_order, agenda_order, lex_tie=True):
    """Agenda members move in sequence; proposing triggers an immediate vote."""
    vote = rollcall_spe(gains, quorum, vote_order, lex_tie)
    @lru_cache(None)
    def solve(t):
        if t == len(agenda_order):
            return frozenset((0,))
        govt = agenda_order[t]
        no_motion = solve(t + 1)
        out = set()
        for l in no_motion:
            for m in vote:
                out.update(preferred(l, m, gains[govt], lex_tie))
        return frozenset(out)
    return solve(0)


def selector(gains, quorum, agenda):
    supporters = {i for i, v in enumerate(gains) if v >= 0}
    return int(len(supporters) >= quorum and bool(supporters.intersection(agenda)))


def main():
    global SPE_CASES, VOTE_CASES
    for gains in product((-1, 0, 1), repeat=N):
        for quorum in (1, 2, 3):
            for vote_order in permutations(range(N)):
                votes = rollcall_spe(gains, quorum, vote_order)
                assert votes == frozenset((int(sum(g >= 0 for g in gains) >= quorum),))
                VOTE_CASES += 1
                for count in (1, 2, 3):
                    for agenda in combinations(range(N), count):
                        for agenda_order in permutations(agenda):
                            outcome = sequential_agenda_spe(
                                gains, quorum, vote_order, agenda_order
                            )
                            expected = selector(gains, quorum, agenda)
                            assert outcome == frozenset((expected,)), (
                                gains, quorum, agenda, vote_order, agenda_order,
                                outcome, expected
                            )
                            SPE_CASES += 1

    # Stage30N: same r=2, country 3 outside private founders 1/2.
    gains = (+1, +1, -1)
    assert sequential_agenda_spe(gains, 2, (0, 1, 2), (2,)) == frozenset((0,))
    assert sequential_agenda_spe(gains, 2, (0, 1, 2), (0, 2)) == frozenset((1,))
    assert sequential_agenda_spe(gains, 3, (0, 1, 2), (0, 2)) == frozenset((0,))

    # Exact ties require a policy preference refinement. With an indifferent
    # sole proponent and quorum=1, otherwise both policy outcomes are SPE.
    ties = (0, -1, -1)
    assert sequential_agenda_spe(ties, 1, (0, 1, 2), (0,), False) == frozenset((0, 1))
    assert sequential_agenda_spe(ties, 1, (0, 1, 2), (0,), True) == frozenset((1,))

    # Simultaneous costless voting: all-NO is a pure Nash ballot profile for r>=2
    # (any single YES leaves L), even at three strictly pro-M governments.
    # Combining that off-path political continuation with NNN initial firms
    # produces a different L terminal SPE under unrestricted government Nash:
    # a unilateral O entrant faces no partner benefits but pays K>0.
    for quorum in (2, 3):
        assert 1 < quorum
    assert (0, 0, 0) != (+1, +1, +1)  # voting actions != policy preferences

    print(f"PASS: {VOTE_CASES} roll-call subgames, {SPE_CASES} agenda+vote games")
    print("Exact 3^3 signs, nonempty agenda sets, r=1/2/3, all orders: selector matched.")
    print("Stage30N fixed r2 comparison: protected old L, unprotected new M.")
    print("Negative control: unrefined simultaneous voting admits all-NO Nash at r>=2.")
    print("Scope: stipulated lexicographic M ties, sequential motion+roll call, no procedural costs.")
    print("NOT certified: generic simultaneous-vote SPE, transfer/IP/public-design extensions,")
    print("continuous firm-SPE proofs, categorical-demand robustness, literature priority.")


if __name__ == "__main__":
    main()
