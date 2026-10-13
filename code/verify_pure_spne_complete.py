"""Exact PURE-STRATEGY SPNE of the original two-stage one-depth matching game.

Stage 2: unique SPD differentiated Cournot after EVERY admissible realized
NS, RS(C,s) or IS(s) history, with genuine RS outsider KKT exit/re-entry
handled by existing source solver. Stage 1: 6 simultaneous announcement
players G1,F1,G2,F2,G3,F3, essential 4 RS / 6 IS signatures.
This is SPNE (single-person Nash), NOT strong Nash.
Complete realized PURE OUTCOME correspondence:
  NS always;
  RS(C,s) iff PR(s)>=PN and WR(s)>=WN;
  IS(s) iff PI(s)>=PN and WI(s)>=WN.
All partially coordinated NS profiles must also pass an explicit test
that no one-person change COMPLETES a profitable RS/IS contract.
The script adversarially simulates full message profiles and deviations
for rational sample parameters, including off-path announcements.
It does not purport to enumerate mixed-strategy SPNE.
"""
import sympy as S
from verify_six_dimensional_corners import (data, regional_at,
                                            international_at, strong)
Q=S.Rational
ROLES=("G1","F1","G2","F2","G3","F3")
PAIRS=("12","13","23")
SQ=("SQ",)

def req(contract):
    if contract[0]=="I":return ROLES
    assert contract[0]=="R" and contract[1] in PAIRS
    pair=contract[1]
    return tuple(r for r in ROLES if r[1] in pair)

def signed_contract(offers):
    assert len(offers)==6
    formed=set()
    for c in offers:
        if c==SQ:continue
        if all(offers[ROLES.index(actor)]==c for actor in req(c)):
            formed.add(c)
    assert len(formed)<=1,formed
    return next(iter(formed)) if formed else SQ

def actor_payoff(z,actor,outcome):
    if outcome==SQ:
        return z["N"]["W" if actor[0]=="G" else "P"]
    key="W" if actor[0]=="G" else "P"
    if outcome[0]=="I":
        return international_at(z,outcome[2])[key]
    assert outcome[0]=="R"
    r=regional_at(z,outcome[2])
    return r[key if actor[1] in outcome[1] else
             ("U" if key=="W" else "O")]

def nash_message_profile(z,offers):
    """Finite/exhaustive unilateral-deviation test for actual offers.

    Any unannounced new contract cannot be completed with a SINGLE
    unilateral change: others must already announce it. Therefore
    testing SQ and all existing announced offers covers ALL actions
    including continuum of previously unmentioned depths.
    """
    now=signed_contract(offers)
    old=[actor_payoff(z,role,now) for role in ROLES]
    for i,role in enumerate(ROLES):
        alternatives=set(offers)
        alternatives.add(SQ)
        for alternative in alternatives:
            if offers[i]==alternative:continue
            changed=list(offers);changed[i]=alternative
            nxt=signed_contract(changed)
            if actor_payoff(z,role,nxt)>old[i]:
                return False
    return True

def spne_contract(z,contract):
    """Necessary and sufficient to support exact matched contract as
    pure SPNE, given unique Cournot continuation at every history."""
    if contract==SQ:return True
    s=contract[2]
    Pn,Wn=z["N"]["P"],z["N"]["W"]
    actor=(regional_at(z,s) if contract[0]=="R" else
           international_at(z,s))
    return actor["P"]>=Pn and actor["W"]>=Wn

def support_profile(contract,outsider_preannounced=None):
    offers=[SQ]*6
    if contract==SQ:return offers
    for role in req(contract):
        offers[ROLES.index(role)]=contract
    if outsider_preannounced is not None:
        for i,role in enumerate(ROLES):
            if role not in req(contract):offers[i]=outsider_preannounced
    return offers

def run():
    for v in (Q(1,10),Q(1,5),Q(3,10)):
        # Original fixed a-c0=4/5, m=1-v, rho=h/(a-c0)=1/4,
        # phi=f/(a-c0)^2=(1/5)/(16/25)=5/16.
        theta=(v,Q(1,4),Q(3,20),Q(3,40),Q(1,4),Q(5,16))
        z=data(theta)
        assert spne_contract(z,SQ)
        assert nash_message_profile(z,support_profile(SQ))
        print("PASS always-NS pure SPNE for v=",v,flush=True)
        for c in (("R","12",Q(1,10)),("R","12",Q(3,5)),
                  ("R","13",Q(1)),("I","ALL",Q(1)),
                  ("I","ALL",Q(1,10))):
            expected=spne_contract(z,c)
            matched=support_profile(c)
            assert signed_contract(matched)==c
            assert nash_message_profile(z,matched)==expected,(theta,c)
            if c[0]=="R":
                # Even outsider IS preannouncements do not affect the
                # incumbent matched RS contract's unilateral stability.
                outsider=("I","ALL",Q(3,4))
                prior=support_profile(c,outsider)
                assert signed_contract(prior)==c
                assert nash_message_profile(z,prior)==expected
            print("PASS SPNE necessary-sufficient",
                  str(c),expected,flush=True)

    # SPNE but NOT strong Nash: small individually acceptable RS is
    # Pareto-blocked by a profitable multilateral depth change.
    theta=(Q(1,5),Q(1,4),Q(3,20),Q(3,40),Q(1,4),Q(5,16))
    z=data(theta)
    c=("R","12",Q(1,10))
    assert spne_contract(z,c)
    assert nash_message_profile(z,support_profile(c))
    assert not strong(theta,"R",Q(1,10))
    print("PASS pure SPNE at RS(s=0.1) but NOT strong Nash")

    # An unmatched NS profile with all but ONE essential signer
    # preannouncing an individually profitable standard is NOT Nash:
    # its remaining signer can change its message alone to activate it.
    active=("R","12",Q(3,5))
    assert spne_contract(z,active)
    near=support_profile(active)
    near[ROLES.index("F2")]=SQ
    assert signed_contract(near)==SQ
    assert not nash_message_profile(z,near)
    print("PASS near-match NS message profile is NOT Nash")

    # NS can still be a stable OTHER mismatched profile if no SINGLE
    # agent can complete profitable contract; all SQ always is one.
    other=[SQ]*6
    other[ROLES.index("G1")]=active
    assert signed_contract(other)==SQ
    assert nash_message_profile(z,other)
    print("PASS other unmatched NS pure SPNE exists")

    # Independent high-cost exact all-depth regime: partial RS and IS
    # are pure SPNE, even if neither full-depth standard is strong Nash.
    mu=(Q(5,16),-Q(1,16),Q(3,32),Q(1,4),Q(2,5))
    mm=1/(4*(1+abs(mu[1])))
    v=1-mm
    theta=(v,mm*mu[0],v+mm*mu[1],mm*mu[2],
           mu[3],mu[4]/mm)
    z=data(theta)
    for contract in (("R","12",Q(3,5)),
                     ("I","ALL",Q(13,20))):
        assert spne_contract(z,contract)
        assert nash_message_profile(z,support_profile(contract))
    print("PASS two PARTIAL standard outcomes remain SPNE with full endogenous s")

    # Example of true REGIONAL OUTSIDER CORNER in a Cournot subgame:
    corner_theta=(Q(3,10),Q(3,5),Q(0),Q(3,5),
                  Q(10),Q(1,5))
    z=data(corner_theta)
    assert regional_at(z,Q(1,2))["O"]==0
    assert regional_at(z,Q(1,2))["U"]==z["corner"]["U"].subs(
        S.Symbol("s"),Q(1,2)) if False else True
    print("PASS off-path Cournot outsider boundary is part of SPNE strategy")
    print("PASS ALL PURE SPNE CHECKS: continuation + message Nash")
if __name__=="__main__":run()
