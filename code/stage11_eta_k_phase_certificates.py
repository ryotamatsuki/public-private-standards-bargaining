"""Stage11: exact eta-K phase bifurcation, 2D SPE coexistence and welfare crossing.
Uses the Stage10 extensive-form governance, Cournot and capital-stock costs.
No claim of an exhaustive 7D parameter equilibrium partition.
"""
import sympy as S
from math import comb
from itertools import product
import stage10_positive_design_endogenous_public_depth_spe as t10
R=S.Rational
m,g,v,k,rho,phi=R(99,100),R(7,50),R(1,100),R(1,50),R(8,25),R(7,50)
a,e,c=S.symbols("a eta c",real=True)
b=g+k*a-v*c;d=g-e*a;z=1+rho*c;A=2*m+b;D=2*m*A-2*d*d
x=S.cancel((2*m*z-d)/D);y=S.cancel((A-2*d*z)/D)
fee=phi*(c*c+a*a)/2
PR=S.cancel(3*m*x*x-fee);PO=S.cancel(3*m*y*y)
CS=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
qi=z/(2*(m+b))
PI=S.cancel(3*m*qi*qi-fee)
WI=S.cancel(PI+R(3,2)*(m+2*b)*qi*qi)
PN=3*m/(4*(m+g)**2)
WN=S.cancel(PN+R(3,2)*(m+2*g)/(4*(m+g)**2))
f=S.cancel(PR.subs(c,1))
W=S.cancel((2*PR+PO+3*CS).subs(c,1))
WIP=S.cancel(WI.subs({a:0,c:1}))
PIP=S.cancel(PI.subs({a:0,c:1}))
eta_on=R(306108,8604325)

def tensor_positive(expr,trans,variables,label):
    n,den=S.fraction(S.cancel(expr.subs(trans,simultaneous=True)))
    if den.subs({q:0 for q in variables})<0:n,den=-n,-den
    ns=[]
    for pol in (n,den):
        p=S.Poly(pol,*variables);deg=p.degree_list();co=p.as_dict();count=0
        for inds in product(*(range(j+1) for j in deg)):
            h=sum(val*S.prod(R(comb(i,j),comb(N,j))
                    for i,j,N in zip(inds,idx,deg))
                    for idx,val in co.items()
                    if all(j<=i for j,i in zip(idx,inds)))
            assert h>0,(label,inds,h)
            count+=1
        ns.append(count)
    print('PASS Bernstein',label,ns,flush=True)

def sturm_positive(expr,q,left,right,label):
    n,den=S.fraction(S.cancel(expr))
    if den.subs(q,left)<0:n,den=-n,-den
    for pol in (n,den):
        p=S.Poly(pol,q)
        assert p.eval(left)>0 and p.eval(right)>0,(label,'endpoint')
        assert p.count_roots(left,right)==0,(label,'root')
    print('PASS Sturm',label,flush=True)

def theorem():
    U,T=S.symbols('U T')
    assert 2*m+g-v-2*g*(1+rho)>0 and m>2*(g+k)
    # RS c-choice globally max=1 for all eta in [0,.14].
    assert S.factor(S.diff(x,c)-2*m*(rho+v*x)/D)==0
    Dmax=2*m*(2*m+g+k)
    assert 6*m*(2*m-g)/Dmax*(2*m*rho/Dmax)>phi
    tensor_positive(-S.diff(f,a,2),{a:U,e:R(7,50)*T},(U,T),'P_aa<0 for all eta')
    tensor_positive(S.diff(f,a,e),{a:U,e:R(7,50)*T},(U,T),'P_aeta>0 for all eta')
    origin=S.factor(S.diff(f,a).subs(a,0))
    assert origin==R(14693184)*(R(8604325)*e-R(306108))/R(221518693813925)
    assert origin.subs(e,eta_on)==0
    assert S.diff(f,a).subs({a:1,e:R(7,50)})<0
    assert S.diff(f,a).subs({a:R(1,4),e:R(1,10)})>0
    assert S.diff(f,a).subs({a:R(61,100),e:R(7,50)})<0
    print('THEOREM aR*=0 for eta<=',eta_on,'and unique increasing',
          'strict interior solution thereafter through eta=.14',flush=True)
    # Uniform ALL-technology, ALL-government-deviation SPE sufficient
    # inequalities of Stage10, now extended from eta=.14 to [.1,.14].
    # f_eta>=0 follows P_aeta>0 and f_eta(eta,0)=0.
    assert S.diff(f,e).subs(a,0)==0
    sturm_positive(R(1009,1000)-f.subs(e,R(7,50)),
                   a,0,1,'uniform RS private max<1.009')
    assert R(1009,1000)-R(27,50)<PN
    Ymin=2*m+g-v-2*g*(1+rho)
    assert PIP-R(27,50)<3*m*(Ymin/Dmax)**2
    # RS outsider at private optimum: eta>=.1,a*>.25.
    Amin=2*m+g-v+k*R(1,4)
    dupper=g-R(1,10)*R(1,4)
    upperD=2*m*(2*m+g+k-v)
    ylower=(Amin-2*dupper*(1+rho))/upperD
    assert ylower==R(3019,7029)
    POutLower=3*m*ylower*ylower
    assert POutLower==R(9114361,16635300)
    # Third private X entrant arbitrary (c3,a3) has q3<.6.
    qcap=R(3,5);Amax=2*m+g+k-v;tmin=g-v;tmax=g+k
    assert Amax*(1+rho-2*m*qcap)-2*tmin*(1+rho-tmax*qcap)<0
    assert 3*m*qcap*qcap-R(27,50)<POutLower
    assert R(1009,1000)-R(27,50)<POutLower
    # Incumbent gov veto after sunk proprietary RS, considering best M.
    xlower=(2*m-g)/Dmax
    CSfloor=(m+g-v)*xlower*xlower
    assert f.subs({e:0,a:0})+CSfloor-WIP+R(27,50)>0
    # After incumbent unilateral N, all 3 gov favor public M.
    assert WIP-WN>R(14,25)
    assert f.subs({e:0,a:0})>PIP
    # Public G1 strictly chooses (cP,aP)=(1,0), all 3 comply for
    # ANY publicly chosen depth; off-path adoption Nash credible.
    public_dloss=3*k*(2*m+b)*z*z/(4*(m+b)**3)+phi*a
    assert S.factor(S.diff(WI,a)+public_dloss)==0
    sturm_positive(S.diff(WI.subs(a,0),c),c,0,1,'public cP=1')
    assert 3/(4*m)-phi>R(14,25)
    for gg in (S.cancel(3*m*(z/(2*m+b))**2-fee),PI):
        sturm_positive(S.diff(S.cancel(gg.subs(a,c)),c),c,0,1,
                       'mandatory adopter global minimum at 0')
        assert gg.subs({a:0,c:0})>R(14,25)
    print('THEOREM full-continuous RS(a*>0) and public optimal IS coexist',
          'for EVERY eta in [.10,.14] and K in [.54,.56]',flush=True)
    # Exact welfare comparison for the TWO ACTUAL equilibria.
    # gap= W_RS(eta,a*(eta))-3 W_I(1,0)+K, strictly increasing
    # in eta and in K on the coexistence rectangle.
    subs={e:R(1,10)+R(1,25)*T,a:R(1,4)+R(9,25)*U}
    tensor_positive(S.diff(W,e),subs,(T,U),'world W_eta>0')
    tensor_positive(S.diff(W,a),subs,(T,U),'world W_a>0')
    for E,low,high,sign in ((R(118,1000),R(4186,10000),R(4187,10000),-1),
                             (R(119,1000),R(4255,10000),R(4256,10000),1)):
        assert S.diff(f,a).subs({e:E,a:low})>0
        assert S.diff(f,a).subs({e:E,a:high})<0
        exposed=high if sign<0 else low
        assert sign*(W.subs({e:E,a:exposed})-3*WIP+R(11,20))>0
    print('THEOREM exactly one social welfare ranking reversal',
          'at K=.55, eta in (.118,.119).',
          'K_world(eta)=3 WI(1,0)-W_RS(eta,a*(eta)) decreasing.',flush=True)

if __name__=="__main__":
    theorem()
    print('Limits: this is a rigorously certified 2D subregion and',
          'an exact private-design bifurcation, NOT a full',
          'seven-dimensional necessary/sufficient equilibrium partition.')
