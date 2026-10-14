"""Stage28 manuscript stop-search gate: mathematical claims vs source-proven facts.

No new economic model or new theorem: validates that draft claims retain
the EXACT frozen Stage26/27 scope, that all 63 institutional cases hold,
that ex-ante / ex-post capital accounting identities hold, and that
the pre-manuscript draft explicitly discusses newly identified PRIOR
ART (Costinot 2008, Ruiz 2004) and publication caveats.

This is a machine-checkable *consistency* gate, not a semantic proof
that the prior-art novelty review is exhaustive or that the model is
independently peer-reviewed. Scientific priority remains human work.
"""
from pathlib import Path
import sympy as S
import stage26_nested_policy_welfare_cutoffs as st26
import stage27_agenda_hitting_set_spe_classification as st27

def manuscript_claim_guard():
    root=Path(__file__).resolve().parent.parent
    manuscript=(root/"docs/manuscript/STAGE28_ABSTRACT_INTRODUCTION_OUTLINE.md").read_text()
    audit=(root/"docs/institutions/STAGE28_NOVELTY_STOP_SEARCH_GATE_20261014.md").read_text()
    for paper in ("Gandal", "Klimenko", "Costinot", "Farrell", "Simcoe", "Ruiz"):
        assert paper in manuscript and paper in audit,paper
    for required in ("pure-strategy", "three-country",
                     "cannot subsequently be recovered",
                     "does not imply", "full published", "mixed"):
        assert required.lower() in manuscript.lower(),required
    for required in ("STOP extension search", "CRITICAL overlap risk",
                     "Full published Gandal", "R2. 3-country combinatorics",
                     "R5. Parameter calibration", "Stage29",
                     "access-restricted"):
        assert required.lower() in audit.lower(),required
    for banned in ("first to endogenize", "first to use a two-vote",
                   "proves majority maximizes welfare"):
        assert banned.lower() not in manuscript.lower()
    print("PASS Stage28 scope / relevant literature / no-firstness claim ledger")

def exact_theorem_trace():
    st26.algebraic_threshold_identities()
    st27.hitting_set_lemma()
    st27.exact_policy_regimes()
    # Every observed privately optimal coalition voting comparison
    # in the draft remains in baseline Stage14 national sign rectangle.
    st26.institutional_policy_matrix()
    # Exact world-welfare identity written in English draft.
    K=S.symbols("K")
    difference=S.cancel((st26.KW-K)-(st26.KE-K))
    assert S.factor(difference-st26.phi*st26.a**2)==0
    # Distinguish pure-SPE TERMINAL outcome unique vs strategy unique:
    # Under q=1,2 and two proposers the NNN profile exists
    # (by Stage27 proof) but off-path histories need not all vote M.
    assert st27.government_policy((S.Integer(1),)*3,{0,1},2)
    assert not st27.government_policy((S.Integer(-1),)*3,{0,1},2)
    print("PASS exact baseline iff agenda threshold and welfare wedge")

if __name__=="__main__":
    manuscript_claim_guard()
    exact_theorem_trace()
    print("STAGE28 GO: proceed to manuscript full draft; STOP speculative",
          "extensions. Priority still CONDITIONAL on inaccessible",
          "Gandal–Shy 2001 and Klimenko 2009 full-text theorem audit.")
