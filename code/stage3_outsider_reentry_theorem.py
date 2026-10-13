"""Stage 3 structural search: endogenous-standardization comparative statics
of outsider zero Cournot output, its reentry, and an ON-EQUILIBRIUM RS witness.

Original one-control NS/RS/IS model, not a new premise. The Stage-1
refinement is STRONG NASH OF CONTRACT ANNOUNCEMENTS conditional on Nash-
Cournot subgame continuation, not strong Nash of whole two-stage game.

All witness checks are EXACT rational Sturm interval proofs, not a grid.
"""
import sympy as S
s=S.symbols("s",real=True)
Q=S.Rational

def sign_on(expr,lo,hi,label):
    """Strict positivity of a rational function on closed rational interval."""
    num,den=S.fraction(S.cancel(expr))
    if den.subs(s,lo)<0:num,den=-num,-den
    for tag,expr_ in (("numerator",num),("denominator",den)):
        p=S.Poly(expr_,s)
        assert p.eval(lo)>0 and p.eval(hi)>0,(label,tag,"endpoints")
        assert p.count_roots(lo,hi)==0,(label,tag,"roots")
    print("PASS continuous",label,flush=True)

def general_proposition():
    v,g,k,e,r=S.symbols("v gamma kappa eta rho",real=True)
    m=1-v
    b=g+(k-v)*s;d=g-e*s
    Y=2*m+b-2*d*(1+r*s)
    C=2*m-g;B=k-v-2*g*r+2*e;D=2*e*r
    assert S.expand(Y-(C+B*s+D*s*s))==0
    assert S.diff(Y,s,2)==2*D
    # Sharp two-crossing regime for 0<s_-<s_+<1, C>0, D>=0:
    # D>0, -2D<B<0, B²>4DC, C+B+D>0.
    # s_{-,+}=(-B +- sqrt(B²-4DC))/(2D)
    # Implicit-function derivative ds_root/dz= -Y_z/Y_s.
    assert S.expand(S.diff(Y,r)+2*s*d)==0
    assert S.expand(S.diff(Y,e)-2*s*(1+r*s))==0
    assert S.expand(S.diff(Y,k)-s)==0
    assert S.expand(S.diff(Y,v)+2+s)==0
    # Hence increasing r stretches the outsider-zero interval if d>0:
    # left root moves left, right root moves right; increasing outsider
    # differentiation eta and member substitution kappa CONTRACTS it;
    # v stretches it, but changes BOTH own demand diagonal and compatibility.
    print("PASS exact 5-dimensional primitive Y polynomial and root derivatives")

def witness_equilibrium():
    v,g,k,e,r,f=Q(3,10),Q(3,5),Q(1,10),Q(11,20),Q(10),Q(120)
    m=1-v
    b=g+(k-v)*s;d=g-e*s
    Delta=S.factor(2*m*(2*m+b)-2*d*d)
    Y=S.factor(2*m+b-2*d*(1+r*s))
    C=Y.subs(s,0);B=S.diff(Y,s).subs(s,0);D=S.diff(Y,s,2)/2
    assert all([D>0,-2*D<B<0,B*B>4*D*C,C+B+D>0])
    low,high=S.solve(Y,s)
    assert 0<low<Q(2,25)<Q(1,10)<Q(93,100)<high<1
    assert S.factor(Y-(110*s*s-111*s+8)/10)==0
    assert S.factor(low-(111-S.sqrt(8801))/220)==0
    assert S.factor(high-(111+S.sqrt(8801))/220)==0
    # Source-demand matrices SPD for ALL s through endpoint test.
    m1=m-(g+k-v)
    mat_safety=(m-g,m+2*g,m1,m+2*(g+k-v),
                m*(m+g+k-v)-2*(g-e)**2)
    assert mat_safety==(Q(1,10),Q(19,10),Q(3,10),
                        Q(3,2),Q(153,200))
    assert all(q>0 for q in mat_safety)
    # Both unique KKT pieces from the original Cournot system.
    x=S.cancel((2*m*(1+r*s)-d)/Delta)
    y=S.cancel(Y/Delta)
    xc=S.cancel((1+r*s)/(2*m+b))
    qi=S.cancel((1+r*s)/(2*(m+b)))
    assert S.factor(x-xc+d*y/(2*m+b))==0
    assert Y.subs(s,Q(1,10))<0
    assert Y.subs(s,0)>0 and Y.subs(s,1)>0
    # Actual producer payoff in output-positive vs outsider-zero branches.
    csr=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
    csc=S.cancel((m+b)*xc*xc)
    pr=S.cancel(3*m*x*x-f*s*s)
    wr=S.cancel(pr+csr)
    pc=S.cancel(3*m*xc*xc-f*s*s)
    wc=S.cancel(pc+csc)
    pi=S.cancel(3*m*qi*qi-f*s*s)
    qn=1/(2*(m+g))
    pn=3*m*qn**2; wn=pn+S.Rational(3,2)*(m+2*g)*qn**2
    sd=Q(1,10)
    P=pc.subs(s,sd);W=wc.subs(s,sd)
    assert P==Q(15398,16335) and W==Q(110194,49005)
    assert P>pn and W>wn
    # The existing matching game's full Stage1 Nash implication:
    # since both required regional firms/governments prefer it to NS,
    # RS(12,s=1/10) is realizable in a PURE SPNE, with the unique Cournot
    # continuation after every alternative contract in all subgames.
    # NEW stronger claim: SAME contract is coalition-stable.
    sign_on(P-pi,Q(0),Q(1),"all IS depths private veto")
    # If outsider is active, strict two roots imply s in [0,2/25)
    # or s in (93/100,1]. The corresponding incumbent government
    # / incumbent firm respectively prevents an RS amendment.
    sign_on(W-wr,Q(0),Q(2,25),"active outsider low s: govt veto")
    sign_on(P-pr,Q(93,100),Q(1),"active outsider high s: firm veto")
    # If outsider is inactive, s<1/10 loses govt welfare (Wc increasing)
    # and s>1/10 loses firm profit (Pc decreasing).
    sign_on(S.diff(wc,s),Q(0),sd,"inactive outsider lower s: welfare increasing")
    sign_on(-S.diff(pc,s),sd,Q(1),"inactive outsider higher s: firm profit falling")
    # Outsider SQ is sufficient for EXISTENCE; with strict P > PI ALL t,
    # incumbent veto even protects against outsiders PREANNOUNCING IS(t).
    print("PASS strong RS(12,s=1/10) in outsider-EXIT regime at all depths")
    print("PASS open primitive neighborhood: strict inequalities and KKT signs")
    print("ROOTS exact",low,high,"N",pn,wn,"R",P,W)

def none_of_network():
    # v=0 demonstrates the two-crossing OUTSIDER Cournot phenomenon
    # is not unique to network externalities. Keep k>0 and eta<g.
    v,g,k,e,r=Q(0),Q(9,10),Q(1,20),Q(17,20),Q(10)
    m=1-v
    b=g+(k-v)*s;d=g-e*s
    Y=S.factor(2*m+b-2*d*(1+r*s))
    C=Y.subs(s,0);B=S.diff(Y,s).subs(s,0);D=S.diff(Y,s,2)/2
    assert D>0 and -2*D<B<0 and B*B>4*D*C and C+B+D>0
    assert all(p>0 for p in
       (m-g,m+2*g,m-(g+k-v),m+2*(g+k-v),
        m*(m+g+k-v)-2*(g-e)**2))
    print("PASS outsider zero/reentry even at ZERO network externality v=0")

if __name__=="__main__":
    general_proposition()
    witness_equilibrium()
    none_of_network()
    print("PASS Stage3 algebraic exit-reentry + equilibrium selection witness")
