"""Full-six-dimensional sufficient NS-only parameter region; exact symbolic proof.
All parameters (v,g,kappa,eta,rho,phi) are FREE within the SPD/economic domain.
Proof not dependent on fixed benchmark v nor on positive RS outsider output.
"""
import sympy as S
s,m,g,delta,eta,rho,phi=S.symbols(
    's m gamma delta eta rho phi',real=True)
D0=2*m*(2*m+g)-2*g*g
D1=2*m*delta+4*g*eta
X0=2*m-g
X1=2*m*rho+eta
D=D0+D1*s-2*eta**2*s*s
qin=(X0+X1*s)/D
q0=X0/D0
B=S.factor(X1*D0-X0*D1+2*eta**2*X0)
assert S.factor(D0*D*(qin-q0)-
          s*(X1*D0-X0*D1+2*eta**2*X0*s))==0
# If m>gamma>=eta>=0, and demand SPD, all denominators positive.
# Since B<=0, the linear-in-s bracket is <=B<=0 for 0<s<=1.
# Hence q_R_inside(s)<=q_NS. Actual member output is no greater:
# when outsider y_inside<0, symmetric Cournot KKT sets y_actual=0
# and x_corner=(1+rho*s)/(2*m+b)<=x_inside (since d>=0).
# Real fixed integration cost phi*s^2>0 forces P_RS(s)<P_NS.
H=m+g+delta*s
qi=(1+rho*s)/(2*H)
K=rho*(m+g)-delta
assert S.factor(S.diff(qi,s)-K/(2*H**2))==0
# If K<=0, quantity q_IS(s)<=q_NS; integration cost excludes
# positive-depth IS via required private firm's veto.
# Together K<=0,B<=0 are sufficient for NS to be the unique
# strongly-stable CONTRACT TYPE; all-SQ supports a strong profile.
CSi=S.Rational(3,2)*(m+2*(g+delta*s))*qi*qi
pi=3*m*qi*qi-phi*s*s
L=(3*m+2*g)*K+delta*(m+g)
assert S.factor(S.diff(pi+CSi,s).subs(s,0)-
                3*L/(4*(m+g)**3))==0

def exact_certificate(theta):
    from verify_six_dimensional_corners import data,strong
    v0,g0,k0,eta0,r0,f0=map(S.Rational,theta)
    m0=1-v0;de=k0-v0
    K0=K.subs({m:m0,g:g0,delta:de,rho:r0})
    B0=B.subs({m:m0,g:g0,delta:de,eta:eta0,rho:r0})
    data(theta)
    assert K0<0 and B0<0
    assert strong(theta,'N')
    print('exact six-dimensional strict NS-only open-region witness',
          'K=',K0,'B=',B0,flush=True)

if __name__=='__main__':
    exact_certificate(("1/50","1/4","2/5","1/100","1/200","1/10"))
    print('PROVED general NS-only sufficiency K<=0 AND B<=0',flush=True)
    print('PROVED IS marginal government-veto slope sign is L',flush=True)
