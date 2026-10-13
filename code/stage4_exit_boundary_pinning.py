"""Stage 4: EXACT Cournot-KKT boundary pinning and public/private veto.

Original six exogenous coordinates; s is the ONLY endogenous standard depth.
No new right, transfer, additional depth control or unilateral regulator is added.
A strong Nash claim is ONLY for the reduced first-stage announcement game.
Independent from the Stage 3 checker (re-derives all quantities and payoffs).
"""
import sympy as S

s = S.symbols("s", real=True)
Q = S.Rational


def strictly_positive(expr, lo, hi, name):
    """Sign-correct Sturm proof on the ENTIRE closed rational interval."""
    numerator, denominator = S.fraction(S.cancel(expr))
    if denominator.subs(s, lo) < 0:
        numerator, denominator = -numerator, -denominator
    for tag, expression in (("numerator", numerator), ("denominator", denominator)):
        polynomial = S.Poly(expression, s)
        assert polynomial.eval(lo) > 0, (name, tag, "left")
        assert polynomial.eval(hi) > 0, (name, tag, "right")
        assert polynomial.count_roots(lo, hi) == 0, (name, tag, "roots")
    print("PASS: strict continuum sign:", name, flush=True)


def main():
    v, gamma, kappa, eta, rho, phi = (
        Q(3, 10), Q(3, 5), Q(1, 10), Q(11, 20), Q(10), Q(140)
    )
    m = 1-v
    b = gamma + (kappa-v)*s
    d = gamma-eta*s
    a = 2*m+b
    z = 1+rho*s
    determinant = S.factor(2*m*a-2*d*d)
    Y = S.expand(a-2*d*z)

    # Strictly positive definite NS, IS and RS, all s in [0,1].
    assert all(t > 0 for t in (
        m-gamma, m+2*gamma, m-(gamma+kappa-v),
        m+2*(gamma+kappa-v),
        m*(m+gamma+kappa-v)-2*(gamma-eta)**2
    ))
    assert S.expand(Y-(Q(8, 10)-Q(111, 10)*s+11*s*s)) == 0
    exit_depth, reentry_depth = S.solve(Y, s)
    assert S.simplify(exit_depth-(111-S.sqrt(8801))/220) == 0
    assert S.simplify(reentry_depth-(111+S.sqrt(8801))/220) == 0
    assert 0 < exit_depth < Q(2,25) < Q(1,10) < Q(93,100) < reentry_depth < 1

    # Cournot KKT continuation; outsider interior versus genuine zero quantity.
    outsider_active = S.cancel(Y/determinant)
    insider_active = S.cancel((2*m*z-d)/determinant)
    insider_corner = S.cancel(z/a)
    assert S.factor(insider_active-insider_corner+d*outsider_active/a) == 0
    assert Y.subs(s,Q(1,10)) < 0

    # Worldwide resident-firm earnings; domestic consumer surplus; national welfare.
    private_active = S.cancel(3*m*insider_active**2-phi*s*s)
    private_corner = S.cancel(3*m*insider_corner**2-phi*s*s)
    cs_active = S.cancel((m+b)*insider_active**2
                         +2*d*insider_active*outsider_active
                         +m*outsider_active**2/2)
    cs_corner = S.cancel((m+b)*insider_corner**2)
    govt_active = S.cancel(private_active+cs_active)
    govt_corner = S.cancel(private_corner+cs_corner)

    is_output = S.cancel(z/(2*(m+b)))
    private_is = S.cancel(3*m*is_output**2-phi*s*s)
    ns_output = 1/(2*(m+gamma))
    private_ns = 3*m*ns_output**2
    govt_ns = private_ns + Q(3,2)*(m+2*gamma)*ns_output**2

    # At both boundaries, the two KKT branches agree in levels, not slopes.
    for t in (exit_depth, reentry_depth):
        assert S.simplify((private_active-private_corner).subs(s,t)) == 0
        assert S.simplify((govt_active-govt_corner).subs(s,t)) == 0
        active_yprime = S.diff(Y,s).subs(s,t)/determinant.subs(s,t)
        private_jump = -6*m*insider_corner.subs(s,t)*d.subs(s,t)*active_yprime/a.subs(s,t)
        govt_jump = -4*m*insider_corner.subs(s,t)*d.subs(s,t)*active_yprime/a.subs(s,t)
        assert S.simplify((S.diff(private_active,s)-S.diff(private_corner,s)).subs(s,t)
                          -private_jump) == 0
        assert S.simplify((S.diff(govt_active,s)-S.diff(govt_corner,s)).subs(s,t)
                          -govt_jump) == 0

    # Global private maximum at exit: intervals COVER the three actual KKT regimes.
    # Rational brackets can overlap a different algebraic branch; the sign checks
    # are on algebraic extensions, not mistaken interior Cournot equilibria.
    strictly_positive(S.diff(private_active,s), Q(0), Q(2,25),
                      "P active rises from 0 to first KKT exit")
    strictly_positive(-S.diff(private_corner,s), Q(7,100), Q(94,100),
                      "P corner falls throughout zero-outsider segment")
    strictly_positive(-S.diff(private_active,s), Q(93,100), Q(1),
                      "P active falls throughout reentry segment")

    Pstar = S.simplify(private_corner.subs(s,exit_depth))
    Wstar = S.simplify(govt_corner.subs(s,exit_depth))
    assert S.simplify(Pstar-Q(4,5))>0
    assert S.simplify(Pstar-private_ns)>0
    assert S.simplify(Wstar-govt_ns)>0
    strictly_positive(Q(4,5)-private_is,Q(0),Q(1),
                      "ALL IS depths private veto: P_IS(s)<4/5<Pstar")

    # Both firms and governments accept exit-depth RS vs NS.
    # All RS depths fail strictly to improve any incumbent firm's global maximum.
    # All IS depths are vetoed by an incumbent firm. Thus RS exit-depth is
    # pure SPNE and strong Nash of the reduced stage-1 announcement game,
    # even against outsider preannouncements. Not strong Nash of Cournot stage 2.
    assert S.simplify(S.diff(private_active,s).subs(s,exit_depth))>0
    assert S.simplify(S.diff(private_corner,s).subs(s,exit_depth))<0
    assert S.simplify(S.diff(govt_active,s).subs(s,exit_depth))>0
    assert S.simplify(S.diff(govt_corner,s).subs(s,exit_depth))>0

    # Government wants to increase s beyond the private stop, including to 0.1.
    strictly_positive(S.diff(govt_corner,s),Q(7,100),Q(1,10),
                      "Govt welfare grows above firm-optimal exit")
    assert S.simplify(govt_corner.subs(s,Q(1,10))-Wstar)>0
    assert S.simplify(Pstar-private_corner.subs(s,Q(1,10)))>0
    # UNSAFE unconstrained extension would incorrectly reverse the comparison.
    assert S.simplify(private_active.subs(s,Q(1,10))-Pstar)>0

    # Government's true GLOBAL preferred RS depth lies strictly inside
    # outsider-zero segment, with participating firm's IR violated.
    strictly_positive(S.diff(govt_active,s),Q(0),Q(2,25),
                      "Govt active grows before first exit")
    strictly_positive(-S.diff(govt_active,s),Q(93,100),Q(1),
                      "Govt active falls after reentry")
    derivative_numerator, _ = S.fraction(S.cancel(S.diff(govt_corner,s)))
    derivative_poly = S.Poly(derivative_numerator,s)
    assert derivative_poly.count_roots(Q(0),Q(1))==1
    assert S.diff(govt_corner,s).subs(s,Q(1737,10000))>0
    assert S.diff(govt_corner,s).subs(s,Q(1738,10000))<0
    assert S.simplify(govt_corner.subs(s,Q(3,20))-Wstar)>0
    assert S.simplify(govt_corner.subs(s,Q(3,20))-
                      govt_corner.subs(s,reentry_depth))>0
    assert S.simplify(private_corner.subs(s,Q(1737,10000))-private_ns)<0

    # Validated local fee band: P'_corner<0<P'_active;
    # W'_corner>0 and W'_active>0. Under base fee 140 these are strict.
    gross_p_a = private_active + phi*s*s
    gross_p_c = private_corner + phi*s*s
    gross_w_c = govt_corner + phi*s*s
    fee_lo = S.simplify(S.diff(gross_p_c,s).subs(s,exit_depth)/(2*exit_depth))
    fee_hi = S.simplify(S.diff(gross_p_a,s).subs(s,exit_depth)/(2*exit_depth))
    fee_gov_hi = S.simplify(S.diff(gross_w_c,s).subs(s,exit_depth)/(2*exit_depth))
    assert S.simplify(fee_lo-phi)<0
    assert S.simplify(fee_hi-phi)>0
    assert S.simplify(fee_gov_hi-phi)>0

    print("PASS EXACT: global boundary-pinned first-stage-strong RS",flush=True)
    print("PASS EXACT: government-private wedge, government unconstrained-best RS is not firm-IR",flush=True)
    print("Boundary =",S.N(exit_depth,15),"; reentry =",S.N(reentry_depth,15))
    print("Pstar =",S.N(Pstar,15),"; Wstar =",S.N(Wstar,15))
    print("P_NS =",private_ns,"; W_NS =",govt_ns)
    print("fee-band =",S.N(fee_lo,14),"< phi <",S.N(fee_hi,14),
          "; govt keeps raising if phi <",S.N(fee_gov_hi,14))


if __name__ == "__main__":
    main()
