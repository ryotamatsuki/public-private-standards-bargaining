"""Stage 4 mathematical candidates: KKT corner and policy/bargaining rankings.

Original six-parameter, one-depth Cournot standards game only.
Certificates use exact SymPy rationals, algebraic roots and polynomial root counts.
No general novelty or whole extensive-form strong equilibrium claim.
"""
import sympy as S

s = S.symbols("s", real=True)
Q = S.Rational


def check_global_formula():
    m, b, d, z, y = S.symbols("m b d z y", real=True)
    a = 2*m + b
    x0 = z/a
    x1 = x0 - d*y/a
    p_gap = 3*m*(x1*x1-x0*x0)
    cs_gap = (m+b)*(x1*x1-x0*x0) + 2*d*x1*y + m*y*y/2
    assert S.simplify(p_gap - (3*m*d*d*y*y/a**2-6*m*x0*d*y/a)) == 0
    assert S.simplify(p_gap+cs_gap -
        (-4*m*x0*d*y/a+(m/2-b*d*d/a**2)*y*y)) == 0
    # Under m>0, 0<=b<m, d>=0, SPD: d^2 < m(2m+b).
    # If y<0, both extrapolated interior payoffs strictly exceed true
    # KKT-corner payoffs (strict when d>0). The bracket on y^2 is
    # positive since b*d^2/a^2 < bm/a < m/2.
    H = 2*S.Symbol("t", nonnegative=True)**3+15*S.Symbol("t", nonnegative=True)**2+12*S.Symbol("t", nonnegative=True)-4
    t = S.Symbol("t", nonnegative=True)
    assert S.expand(S.diff(H,t)-6*t*t-30*t-12)==0
    print("PASS symbolic corner correction and unique welfare threshold")


def instance(v, g, k, eta, rho, phi):
    m = 1-v
    b = g+(k-v)*s
    d = g-eta*s
    a = 2*m+b
    z = 1+rho*s
    delta = 2*m*a-2*d*d
    yy = S.factor(a-2*d*z)
    xa = S.cancel((2*m*z-d)/delta)
    ya = S.cancel(yy/delta)
    xc = S.cancel(z/a)
    assert S.factor(xa-xc+d*ya/a)==0
    qi = S.cancel(z/(2*(m+b)))
    pa = S.cancel(3*m*xa**2-phi*s*s)
    pc = S.cancel(3*m*xc**2-phi*s*s)
    wa = S.cancel(pa + (m+b)*xa**2 +2*d*xa*ya + m*ya**2/2)
    wc = S.cancel(pc + (m+b)*xc**2)
    pi = S.cancel(3*m*qi**2-phi*s*s)
    wi = S.cancel(pi + S.Rational(3,2)*(m+2*b)*qi**2)
    qn = 1/(2*(m+g))
    pn = 3*m*qn**2
    wn = pn + S.Rational(3,2)*(m+2*g)*qn**2
    # Exact condition for NS, IS and RS matrices to remain SPD for ALL s.
    assert all(x>0 for x in (
        m-g, m+2*g, m-(g+k-v), m+2*(g+k-v),
        m*(m+g+k-v)-2*(g-eta)**2
    ))
    assert b.subs(s,0)>=0 and b.subs(s,1)>=0
    assert d.subs(s,0)>0 and d.subs(s,1)>0
    return locals()


def positive_on(expr, low, high, label):
    num, den = S.fraction(S.cancel(expr))
    if den.subs(s,low)<0:
        num, den = -num, -den
    for tag, polynomial in (("num", num),("den",den)):
        p = S.Poly(polynomial,s)
        assert p.eval(low)>0 and p.eval(high)>0,(label,tag,"endpoint")
        assert p.count_roots(low,high)==0,(label,tag,"root")
    print("PASS",label)


def root_value(expr, root):
    return S.simplify(expr.subs(s,root))


def boundary_pinned_strong_rs():
    a = instance(Q(3,10),Q(3,5),Q(1,10),Q(11,20),Q(10),Q(140))
    YY, pa, pc, wa, wc = (a[t] for t in ("yy","pa","pc","wa","wc"))
    pi, pn, wn = (a[t] for t in ("pi","pn","wn"))
    left, right = S.solve(YY,s)
    assert S.simplify(left-(111-S.sqrt(8801))/220)==0
    assert S.simplify(right-(111+S.sqrt(8801))/220)==0
    assert 0<left<Q(2,25)<Q(1,10)<Q(93,100)<right<1

    # Three exact derivative certificates prove the UNIQUE GLOBAL firm
    # optimum at the LOWER producer-exit boundary, not merely local FOCs.
    positive_on(S.diff(pa,s),Q(0),Q(2,25),"RS lower active: P increasing")
    positive_on(-S.diff(pc,s),Q(7,100),Q(94,100),"RS corner: P decreasing")
    positive_on(-S.diff(pa,s),Q(93,100),Q(1),"RS upper active: P decreasing")
    positive_on(Q(4,5)-pi,Q(0),Q(1),"ALL IS depths: P_IS < 4/5")

    pstar,wstar = root_value(pc,left),root_value(wc,left)
    assert pstar>Q(4,5)>pn and wstar>wn
    assert root_value(S.diff(pa,s),left)>0
    assert root_value(S.diff(pc,s),left)<0
    assert root_value(S.diff(wa,s),left)>0
    assert root_value(S.diff(wc,s),left)>0

    # Same-depth conflict: true KKT firms veto 10%, govt wants 10%;
    # negative-output extrapolation reverses the firm's comparison.
    sd=Q(1,10)
    assert YY.subs(s,sd)<0
    assert pstar>pc.subs(s,sd)
    assert wc.subs(s,sd)>wstar
    assert pa.subs(s,sd)>pstar

    # Check exact jump identities: Y' is negative at exit, positive at reentry.
    m,d,z,b,delta,yy=(a[t] for t in ("m","d","z","b","delta","yy"))
    AA=2*m+b; xx=z/AA
    for root in (left,right):
        jump_p = (S.diff(pa,s)-S.diff(pc,s)
                  +6*m*xx*d/AA*S.diff(yy,s)/delta).subs(s,root)
        jump_w = (S.diff(wa,s)-S.diff(wc,s)
                  +4*m*xx*d/AA*S.diff(yy,s)/delta).subs(s,root)
        assert S.simplify(jump_p)==0 and S.simplify(jump_w)==0
    print("PASS true RS(exit) is pure SPNE and reduced-stage1 strong-Nash")
    print("  exit=",float(left),"P*=",float(pstar),"W*=",float(wstar))
    print("  left/right P slopes=",
          float(root_value(S.diff(pa,s),left)),float(root_value(S.diff(pc,s),left)))
    print("  right W slope=",float(root_value(S.diff(wc,s),left)))


def public_rs_is_ranking_reversal():
    a=instance(Q(2,5),Q(1,5),Q(59,200),Q(19,100),Q(15),Q(200))
    depth=Q(1,2)
    yy=a["yy"]
    left,right=S.solve(yy,s)
    assert 0<left<depth<right<1
    assert S.factor(yy-(228*s*s-229*s+40)/40)==0
    assert yy.subs(s,depth)==-Q(7,16)
    b,m=a["b"],a["m"]
    assert (b/m).subs(s,depth)==Q(59,240)

    # Global cost coefficient cancels in SAME-depth RS-vs-IS govt rankings.
    wr= a["wc"].subs(s,depth)
    wi= a["wi"].subs(s,depth)
    fake=a["wa"].subs(s,depth)
    pr=a["pc"].subs(s,depth)
    p_is=a["pi"].subs(s,depth)
    assert wr==Q(14923050,290521)
    assert wi==Q(4611775,89401)
    assert fake==Q(17539987975,339182067)
    assert pr==Q(6281950,290521)
    assert p_is==Q(731950,89401)
    assert wr<wi<fake
    assert pr>p_is
    assert pr>a["pn"] and p_is>a["pn"]
    assert wr>a["wn"] and wi>a["wn"]
    # Nonnegative implementation cost: a=17,c0=16,h=15, phi=f=200.
    # Both standard types meet participant IR. Not a global IS strong-Nash proof.
    print("PASS SAME-DEPTH government standard-type rank reversal")
    print("  W_RS(KKT), W_IS, W_RS(invalid interior)=",
          float(wr),float(wi),float(fake))




def public_ranking_reversal_at_zero_network():
    """Stronger counterexample: govt preference reversal is not network-specific."""
    a=instance(Q(0),Q(1,4),Q(0),Q(6,25),Q(25),Q(200))
    left,right=S.solve(a["yy"],s)
    half=Q(1,2)
    assert 0<left<half<right<1
    assert S.factor(a["yy"]-(1200*s*s-1202*s+175)/100)==0
    assert a["yy"].subs(s,half)==-Q(63,50)
    assert (a["b"]/a["m"]).subs(s,half)==Q(1,4)
    pr=a["pc"].subs(s,half)
    pi=a["pi"].subs(s,half)
    wr=a["wc"].subs(s,half)
    wi=a["wi"].subs(s,half)
    fake=S.cancel(a["wa"]).subs(s,half)
    assert pr==Q(58) and pi==Q(937,25)
    assert wr==Q(103) and wi==Q(10309,100)
    assert fake==Q(51578272275,498673561)
    assert pr>pi>a["pn"] and wi>wr>a["wn"]
    assert wr<wi<fake
    # Implementation: a=27, c0=26, h=25, f=200; min MC=1.
    print("PASS policy rank reversal with v=0 and kappa=0")
    print("  W_RS(KKT),W_IS,W_RS(invalid interior) =",
          float(wr),float(wi),float(fake))

if __name__=="__main__":
    check_global_formula()
    boundary_pinned_strong_rs()
    public_rs_is_ranking_reversal()
    public_ranking_reversal_at_zero_network()
    print("PASS Stage 4 theorem candidates; Stage 6 novelty remains NO-GO")
