"""Stage4A second clean-room proof: ALL CONTINUOUS STANDARD DEPTHS.

Stage 2 Cournot derived by direct SYMPY 3x3 matrix inversion, NOT by
previous economic model's closed-form formulas. All continuous t∈[0,1]
sign inequalities certified with exact rational polynomial Sturm root
counts; no grids, no floating tolerance, no old strong() function.
Market 4D normalized coordinates fixed to (G,L,E,rho) =
(5/16,-1/16,3/32,1/4), fees F=.4 and 10 respectively.
Does NOT certify the entire 5D parameter domain.
"""
import sympy as S
s=S.symbols("s",real=True)
Q=S.Rational
g=Q(5,16);lam=-Q(1,16);eta=Q(3,32);rho=Q(1,4)
b=g+lam*s;d=g-eta*s
mat=S.Matrix([[1,b,d],[b,1,d],[d,d,1]])
rhs=S.Matrix([1+rho*s,1+rho*s,1])
quant=(mat+S.eye(3)).inv()*rhs
x=S.cancel(quant[0]);y=S.cancel(quant[2])
assert S.factor(quant[1]-quant[0])==0
qi=S.cancel((1+rho*s)/(2*(1+b)))
qn=1/(2*(1+g))
csr=S.cancel((quant.T*mat*quant)[0]/2)
csi=S.cancel(Q(3,2)*(1+2*b)*qi*qi)
csn=S.cancel(Q(3,2)*(1+2*g)*qn*qn)

def positive_all(expr,label):
    n,den=S.fraction(S.cancel(expr))
    if den.subs(s,0)<0:n,den=-n,-den
    for poly,name in ((n,"NUM"),(den,"DEN")):
        p=S.Poly(poly,s)
        # Strip known factor s^k ONLY from an exact zero at s=0,
        # valid when the theorem asserts strict positivity for s>0.
        while p.eval(0)==0:
            p=S.Poly(S.cancel(p.as_expr()/s),s)
        assert p.eval(0)>0,(label,name,"s=0",p.eval(0))
        assert p.eval(1)>0,(label,name,"s=1",p.eval(1))
        assert p.count_roots(0,1)==0,(label,name,p.intervals())
    print("PASS exact continuum",label,flush=True)

def certify(fee,rs,ii):
    pr=S.cancel(3*x*x-fee*s*s);wr=S.cancel(pr+csr)
    pi=S.cancel(3*qi*qi-fee*s*s);wi=S.cancel(pi+csi)
    pn=S.cancel(3*qn*qn);wn=S.cancel(pn+csn)
    for name,expr in (
        ("RS SPD inner eigen",1-b),
        ("RS SPD 2x2 minor",1+b-2*d*d),
        ("RS outside output positive",y),
        ("RS inside output positive",x),
        ("IS SPD common eigen",1+2*b)):
        positive_all(expr,name)
    # Under RS, ALL possible IS depths are rejected by incumbent
    # member firms: private profit at RS(rs) dominates EVERY PI(t).
    positive_all(S.cancel(pr.subs(s,rs)-pi),
                 "RS member firm vetoes ALL IS depths")
    # Under IS, ALL possible RS depths are rejected by required
    # member governments: their WI(ii) dominates EVERY WR(t).
    positive_all(S.cancel(wi.subs(s,ii)-wr),
                 "IS member govt vetoes ALL RS depths")
    # Within-type joint renegotiation cannot help both signers:
    # each strictly concave and chosen candidate is strictly between
    # the privately optimal and government-optimal depths.
    for name,fun in (("PR",pr),("WR",wr),("PI",pi),("WI",wi)):
        positive_all(-S.diff(fun,s,2),"strict concavity "+name)
    assert S.diff(pr,s).subs(s,rs)<0<S.diff(wr,s).subs(s,rs)
    assert S.diff(pi,s).subs(s,ii)<0<S.diff(wi,s).subs(s,ii)
    # Any one of four/six signers can abort to NS; strict IR holds.
    for expr in (pr.subs(s,rs)-pn,wr.subs(s,rs)-wn,
                 pi.subs(s,ii)-pn,wi.subs(s,ii)-wn):
        assert expr>0
    # Note: unlike matched outcome tests, this check avoids standard
    # comparator/source verifier entirely. It is a robust RS certificate,
    # including even preannounced IS by BOTH RS outsiders.
    print("PASS mathematically independent all-depth pair",fee,rs,ii,
          flush=True)

if __name__=="__main__":
    certify(Q(2,5),Q(3,5),Q(13,20))
    certify(Q(10),Q(17,1000),Q(11,500))
    print("PASS two exact full continuum independent Cournot/Sturm witnesses")
