"""Stage10. Conditional full-CONTINUOUS RS/IS coexistence with positive private
common design, plus genuinely optimized public cP,aP after legislative
authorization. Publicly implementable OPEN family O(cP,aP) is an EXPLICIT
new feasibility assumption. Technical rights X/Y cannot be confiscated.
Original six theta =(.01,.14,.02,.14,.32,.14); real setup K in [.54,.56].
Stage8 irreversible installed-capital cost retained.
All below are rational global continuum certificates, NOT a 7D partition.
"""
import sympy as S
from itertools import product
from math import comb
from fractions import Fraction as F
import stage5_integrated_independent_standards_and_government as core
import stage8_capitalized_retrofit_continuous_is_spe as st8
R=S.Rational
m,g,v,k,e,rho,phi=R(99,100),R(7,50),R(1,100),R(1,50),R(7,50),R(8,25),R(7,50)
c,a=S.symbols('c a',real=True)
lo,hi=R(27,50),R(14,25)
al,ah=R(5949,10000),R(5950,10000)
b=g+k*a-v*c;d=g-e*a;z=1+rho*c;A=2*m+b;D=2*m*A-2*d*d
x=S.cancel((2*m*z-d)/D);y=S.cancel((A-2*d*z)/D)
fee=phi*(c*c+a*a)/2
PR=S.cancel(3*m*x*x-fee);PO=S.cancel(3*m*y*y)
CSR=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
qI=z/(2*(m+b));PI=S.cancel(3*m*qI*qI-fee)
CSI=S.cancel(R(3,2)*(m+2*b)*qI*qI)
WI=S.cancel(PI+CSI);WIs=S.factor(WI.subs({c:1,a:0}))
PIs=S.factor(PI.subs({c:1,a:0}))
PN=3*m/(4*(m+g)**2)
WN=S.cancel(PN+R(3,2)*(m+2*g)/(4*(m+g)**2))

def positive(expr,xx,l,h,name):
    n,dn=S.fraction(S.cancel(expr))
    if dn.subs(xx,l)<0:n,dn=-n,-dn
    for part,p in (('n',n),('d',dn)):
        p=S.Poly(p,xx)
        assert p.eval(l)>0 and p.eval(h)>0,(name,part,'end')
        assert p.count_roots(l,h)==0,(name,part,'roots')
    print('PASS exact rational full interval:',name,flush=True)

def private_ideal():
    assert m>2*(g+k)
    ymin=2*m+(g-v)-2*g*(1+rho)
    dmax=2*m*(2*m+g+k)
    assert ymin>0 and m*(m+g-v)-2*g*g>0
    assert S.factor(S.diff(x,c)-2*m*(rho+v*x)/D)==0
    assert 6*m*(2*m-g)/dmax*(2*m*rho/dmax)>phi
    f=S.cancel(PR.subs(c,1))
    n,den=S.fraction(S.cancel(S.diff(f,a)))
    if den.subs(a,0)<0:n,den=-n,-den
    p=S.Poly(n,a)
    assert S.Poly(den,a).count_roots(0,1)==0
    assert p.count_roots(0,1)==1
    assert p.eval(0)>0 and p.eval(1)<0
    assert p.eval(al)>0 and p.eval(ah)<0
    positive(R(1009,1000)-f,a,0,1,'PR* <1.009')
    positive(f-PIs,a,al,ah,'private positive-a RS better than IS')
    positive(PO.subs(c,1)-R(13,20),a,al,ah,'outsider profit >.65')
    aa=next(float(S.re(t)) for t in S.nroots(p,maxsteps=400)
            if abs(float(S.im(t)))<1e-8 and 0<float(S.re(t))<1)
    print('PROVED a* in (.5949,.5950), numerical',aa,flush=True)
    return f,aa

def public_ideal_and_dominance():
    # Among fully adopting firms, derivative of national W in a
    # negative throughout the physically admissible triangle.
    loss=3*k*(2*m+b)*z*z/(4*(m+b)**3)+phi*a
    assert S.factor(S.diff(WI,a)+loss)==0
    assert m>0 and k>0 and g-v>0
    positive(S.diff(WI.subs(a,0),c),c,0,1,
             'W_public(c,0) strictly rising, unique cP=1')
    # public mandate M(cP,aP) retains unique all-compliance Nash for
    # EVERY 0<=aP<=cP<=1 and K∈[.54,.56], even if all others exit.
    assert 3/(4*m)-phi>hi # one complier
    for nn,ex in ((2,S.cancel(3*m*(z/(2*m+b))**2-fee)),
                  (3,PI)):
        # At fixed c, a increases b and resource expense: min at a=c.
        loss_a=6*m*k*(z/(2*m+b))**2/(2*m+b)+phi*a if nn==2 else (
                6*m*k*qI*qI/(m+b)+phi*a)
        assert S.factor(S.diff(ex,a)+loss_a)==0
        positive(S.diff(S.cancel(ex.subs(a,c)),c),c,0,1,
                 'public n='+str(nn)+' net profit rises on a=c')
        assert ex.subs({c:0,a:0})>hi
    assert WIs-WN>hi
    print('PASS public regulator optimizes continuum at (cP,aP)=(1,0)',
          'and ALL mandate adopters have strictly dominant compliance',
          flush=True)

def outsider_join_any_design():
    # private RS incumbents c1=c2=1, a1=a2=a*>0; arbitrary outsider
    # privately selects (c3,a3). Its cross-similarity t belongs
    # [g-v,g+k]; entrant z3<=1+rho; incumbent pair b12<=g+k-v.
    # Formula q3=(A0*z3-2*t*(1+rho))/(2*m*A0-2*t^2).
    tmin,tmax=g-v,g+k
    Amax,Amin=2*m+g+k-v,2*m+g-v
    Q=R(3,5); Z=1+rho
    ub=S.factor(Amax*(Z-2*m*Q)-2*tmin*(Z-tmax*Q))
    assert ub<0 and Amin-2*tmax*Z>0
    assert 2*m*Amin-2*tmax*tmax>0
    # q3<.6 regardless of entrant's continuum; incumbent output>0
    assert Z-tmax*Q>0
    assert 3*m*Q*Q-lo<R(13,20)
    print('PASS ALL newcomer X technology (c3,a3) deviates:',
          'q3<0.6, entrant net <0.65 < legacy outsider',flush=True)

def main_theorem():
    f,astar=private_ideal()
    public_ideal_and_dominance()
    outsider_join_any_design()
    # Certification of unilateral O developer when other 2 were N:
    # If one N joins, its privately adopted profit <=PR*-K<PN.
    # If the other N joins, its adoption payoff <=PI*-K
    # while its legacy outsider payoff is globally >=gross y_min.
    ymin=2*m+g-v-2*g*(1+rho)
    dmax=2*m*(2*m+g+k)
    lower_out=3*m*(ymin/dmax)**2
    assert R(1009,1000)-lo<PN
    assert PIs-lo<lower_out
    # Uniform government mandate maximum at cP=1,aP=0:
    # private RS X investments are sunk and cannot be recouped;
    # public from X requires an ADDITIONAL family implementation.
    gov_veto=S.cancel(f+CSR.subs(c,1)-WIs+lo+
                       phi*(1+a*a)/2)
    positive(gov_veto,a,al,ah,
             'all public specifications are vetoed after private RS')
    # If either incumbent defects to N, public gov unanimity changes:
    assert WIs-WN>hi
    # No incumbent gains: retaining X <=PR*, other family under C
    # <=PR*, under M <=PI*, and deviating N triggers public M.
    positive(f-PIs,a,al,ah,'incumbents prefer private RS to public IS')
    # No outsider gains by joining X (bound above), by starting O/Y
    # and joining an RS group under certification, or by public M:
    assert R(1009,1000)-lo<R(13,20)
    assert PIs-lo<R(13,20)
    # At NNN, government mandates its optimal (1,0), with unanimous
    # W gain, and any lone private developer cannot beat PI*-K:
    # if M, old OPEN stock+upgrade >= one-shot public investment;
    # if L/C after lone O, remains singleton and earns PN-K-fee.
    assert PN<PIs
    # Aggregate national W under RS vs public IS:
    # 2 member W + outsider W - 3 IS W
    # =2PR+PO+3CSR-3WIstar+K, minimum at K=lo.
    rs_minus_is=S.cancel(2*f+PO.subs(c,1)+3*CSR.subs(c,1)
                         -3*WIs+lo)
    positive(rs_minus_is,a,al,ah,'WORLD welfare RS > IS at all K')
    print('PASS THEOREM: for ALL real K in [27/50,14/25],',
          'full continuous RS(a*>0) and public optimal-depth IS SPE',
          'BOTH exist, with genuine three-government policy',flush=True)
    print('example K=.55, welfare RS',
          float((2*f+PO.subs(c,1)+3*CSR.subs(c,1)-2*R(55,100))
                .subs(a,R(str(astar)))),
          'IS',float(3*(WIs-R(55,100))),flush=True)
    return astar

def fraction_crosscheck(aa):
    # Independently verify 3x3 Cournot/KKT and sampled policy votes,
    # not used to replace the analytic whole-continuum proof.
    st8.freeze_retrofit()
    K=F(11,20);theta=F(7,50)
    X=('X',F(1),F(119,200)) # rational bracket approximation
    h=(X,X,core.N)
    L=core.continuation(h,'L',None,(0,0,0),K,theta)
    assert L[2][2]>0
    for p_c,p_a in ((F(1),F(0)),(F(1),F(1)),
                    (F(1,2),F(0)),(F(3,4),F(1,2))):
        pp=('O',p_c,p_a)
        for pre in (h,(core.N,core.N,core.N),(core.N,X,core.N)):
            ens=core.adoption_pure_nash(pre,'M',pp,K,theta)
            assert len(ens)==1 and ens[0][0]==(1,1,1)
            if pre==h:
                assert ens[0][1][1][0]<L[1][0]
    for lab in ('X','Y','O'):
        for cc,ac in ((F(1,100),F(0)),(F(1),F(0)),
                      (F(1),F(3,5)),(F(99,100),F(1,2))):
            h2=(X,X,(lab,cc,ac))
            pp=core.government_policy(h2,K,theta)[0]
            assert pp[3][0][2]<=L[0][2]
    print('PASS independent Fraction KKT checks at rational .595',
          flush=True)

if __name__=='__main__':
    q=main_theorem()
    fraction_crosscheck(q)
    print('LIMITS: public continuum is legally exogenous; govt agenda',
          'and postauthorization G1 design delegation assumed;',
          'not global seven-dimensional phase diagram.')
