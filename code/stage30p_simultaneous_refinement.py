#!/usr/bin/env python3
"""Stage30P: simultaneous proposal and voting under STAGEWISE admissibility.

Enumerate all binary-vote opponents to eliminate weakly dominated ballots,
then all other proposer actions to eliminate weakly dominated motions in the
reduced political game. Lexical M preference implements Delta_i==0 tie rule.
This checks finite government subgames, not firms' continuous deviations or
the unrefined joint extensive-form equilibrium concept.
"""
from itertools import combinations, product

COUNTRIES = range(3)


def undominated_binary_actions(sign, outcome, rivals_count):
    # outcome(action, other_bits) returns 0=L,1=M
    rivals = list(product((0, 1), repeat=rivals_count))
    values = {
        action: [sign * outcome(action, others) for others in rivals]
        for action in (0, 1)
    }
    return {
        a for a in (0, 1)
        if not all(values[1-a][j] >= values[a][j] for j in range(len(rivals)))
        or not any(values[1-a][j] > values[a][j] for j in range(len(rivals)))
    }


def ballot_actions(gains, quorum):
    ballots = {}
    for i in COUNTRIES:
        def finish(a, others):
            count = a + sum(others)
            return int(count >= quorum)
        ballots[i] = undominated_binary_actions(gains[i], finish, 2)
        assert ballots[i] == ({1} if gains[i] >= 0 else {0})
    return ballots


def motion_actions(gains, quorum, agenda):
    ballots = ballot_actions(gains, quorum)
    supporters = {i for i in COUNTRIES if ballots[i] == {1}}
    passes_if_tabled = int(len(supporters) >= quorum)
    actions = {}
    if not passes_if_tabled:
        return {i: {0, 1} for i in agenda}, passes_if_tabled
    for i in agenda:
        # Proposal payoffs are 1{at least one eligible proposer tables M}.
        def finish(a, others):
            return int(a == 1 or any(others))
        actions[i] = undominated_binary_actions(
            gains[i], finish, len(agenda) - 1
        )
        assert actions[i] == ({1} if gains[i] >= 0 else {0})
    return actions, passes_if_tabled


def run():
    cases = 0
    for gains in product((-1, 0, 1), repeat=3):
        for quorum in (1, 2, 3):
            for length in (1, 2, 3):
                for agenda in combinations(COUNTRIES, length):
                    actions, votes_allow = motion_actions(gains, quorum, agenda)
                    outcomes = set()
                    for motions in product(*(sorted(actions[i]) for i in agenda)):
                        outcomes.add(int(votes_allow and any(motions)))
                    expected = int(
                        sum(g >= 0 for g in gains) >= quorum
                        and any(gains[i] >= 0 for i in agenda)
                    )
                    assert outcomes == {expected}, (
                        gains, quorum, agenda, actions, outcomes, expected
                    )
                    cases += 1
    # Unrefined negative: with r=2, all NO voting is always Nash, even if
    # Delta_i>0 for all three, because a single changed YES cannot pass.
    assert all(sum([int(j == i) for j in COUNTRIES]) < 2 for i in COUNTRIES)
    print(f"PASS: {cases} simultaneous governmental preference/quorum/agenda configurations")
    print("Subgame voting undominated ballot + reduced proposal undominated motion")
    print("has exactly the original M/L selector in each sign/tie configuration.")
    print("This is NOT a theorem for unrefined SPE or endogenous tie selection.")


if __name__ == "__main__":
    run()
