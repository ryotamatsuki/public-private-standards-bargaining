"""Stage 6 absorption check: NO OLIGOPOLY/NETWORK needed for coexistence.

Generic continuous named-standards unanimity contract game with 3 states
and 3 firms, two types RS/IS and strictly private/public different goals.
Payoffs are NOT derived from Cournot or network goods. The same source
stage-1 exact-matching protocol is retained. This shows that mere RS/IS
coexistence and 1/F partial-depth fee response do not REQUIRE the proposed
network-substitution microfoundation.

For any fee F>=7/2, example payoff functions:
  P_R(s)=5s-Fs^2, W_R(s)=1+6s-Fs^2;
  P_I(s)=4s-Fs^2, W_I(s)=1+7s-Fs^2;
  P_N=0, W_N=1, P_O=0, U_O=1.
Use consumer-surplus interpretations CS_R=1+s, CS_I=1+3s,
so govt = firm profit + consumer surplus exactly; CS positive.
  s_R=5/(2F), maximizes private P_R globally
  s_I=7/(2F), maximizes national W_I globally.
Exact algebraic square-completion gives:
  max_s P_R=25/(4F) > max_s P_I=16/(4F),
  max_s W_I=1+49/(4F) > max_s W_R=1+36/(4F);
  W_R(s_R)-W_N=35/(4F)>0,
  P_I(s_I)-P_N=7/(4F)>0.
Thus for EVERY arbitrarily large F>=7/2, RS(s_R) AND IS(s_I)
are reduced-first-stage strong Nash, RS robustly so regardless of
unmatched outsider preannouncements. Same partner-group SPNE criteria
hold; both s lie within allowed [0,1]. In nested firm-only game only
RS structure stable; in nested government-only only IS structure
stable, provided outsider IR as above. Hence even nested-structure
disagreement with joint-type coexistence need not require network,
Cournot or endogenous product substitutability.
"""
import sympy as S

f,t=S.symbols("F s",real=True,positive=True)
sr=S.Rational(5,2)/f; si=S.Rational(7,2)/f
PR=5*t-f*t*t
PI=4*t-f*t*t
WR=1+6*t-f*t*t
WI=1+7*t-f*t*t
PN=S.Integer(0);WN=S.Integer(1)
OR=S.Integer(0); UR=S.Integer(1)
assert S.simplify(WR-PR-(1+t))==0
assert S.simplify(WI-PI-(1+3*t))==0
assert S.simplify((PR.subs(t,sr)-PR)-f*(t-sr)**2)==0
assert S.simplify((PI.subs(t,2/f)-PI)-f*(t-2/f)**2)==0
assert S.simplify((WR.subs(t,3/f)-WR)-f*(t-3/f)**2)==0
assert S.simplify((WI.subs(t,si)-WI)-f*(t-si)**2)==0

# Strict global cross-standard veto inequalities, all depth t >= 0:
assert S.simplify((PR.subs(t,sr)-PI) -
                  (S.Rational(9,4)/f+f*(t-2/f)**2))==0
assert S.simplify((WI.subs(t,si)-WR) -
                  (S.Rational(13,4)/f+f*(t-3/f)**2))==0
assert S.simplify(WR.subs(t,sr)-WN-S.Rational(35,4)/f)==0
assert S.simplify(PI.subs(t,si)-PN-S.Rational(7,4)/f)==0
assert S.simplify(PR.subs(t,sr)-PN-S.Rational(25,4)/f)==0
assert S.simplify(WI.subs(t,si)-WN-S.Rational(49,4)/f)==0

# Under f>=7/2, all ideal depths <=1; both are POSITIVE; exact
# squares above rule out every same-type and opposite-type deviation.
for fee in (S.Rational(7,2),S.Rational(10),S.Rational(1000)):
    X=sr.subs(f,fee);Y=si.subs(f,fee)
    assert 0<X<=1 and 0<Y<=1
    assert PR.subs({f:fee,t:X})>PN
    assert WR.subs({f:fee,t:X})>WN
    assert PI.subs({f:fee,t:Y})>PN
    assert WI.subs({f:fee,t:Y})>WN
    print("PASS abstract-coalition coexistence F=",fee,
          "regional-depth=",X,"universal-depth=",Y,flush=True)
print("PROVED full-continuum identities: network, Cournot, substitution absent")
print("Stage6 absorption: COEXISTENCE/1-F PARTIAL-DEPTH mechanism generic")
