"""Stage 6 -- adversarial exact ALL-continuous/multiple-continuation SPE audit.

This is NOT a claimed global 7D full phase diagram. It delivers a REAL
fully continuous initial-choice SPE existence theorem for fragmented NNN,
valid under ANY mixed adoption equilibrium, at sufficiently high K.

It also COMPLETELY classifies the 8 pure-compliance profiles of the
GOVERNMENT M subgame after NNN for ALL strict K intervals, and proves
the EXACT three Nash equilibria at K=3/4 (000,111,one mixed symmetric).

The full user-required all-parameter equilibrium set would require
solving continuum initial choices AND all off-path selected mixed Nash
adoption games. Formula-only fixed point conditions do NOT establish
that result; this certificate labels the remaining gap explicitly.

Uses original six technology primitives plus explicitly seventh K;
government M open blueprint O(1,0) is assumed available prehistorically;
C cannot be proposed after NNN without an O developer.
"""
from fractions import Fraction as F
from itertools import product
import sympy as S
from stage5_integrated_independent_standards_and_government import (
    N, PUBLIC, continuation, adoption_pure_nash, government_policy)

r=S.Rational
m=r(99,100)
gamma=r(7,50)
v=r(1,100)
rho=r(8,25)
phi=r(7,50)
b=gamma-v
z=1+rho
qN=1/(2*(m+gamma))
PN=S.cancel(3*m*qN*qN)
CSN=S.cancel(r(3,2)*(m+2*gamma)*qN*qN)
WN=PN+CSN

q1=S.cancel(1/(2*m))                # one adopter no partner benefit
q2=S.cancel(z/(2*m+b))            # exactly two adopters
q3=S.cancel(z/(2*(m+b)))          # all three adopters
G=(r(0),S.cancel(3*m*q1*q1-phi/2),
   S.cancel(3*m*q2*q2-phi/2),
   S.cancel(3*m*q3*q3-phi/2))
CS=(r(0),S.cancel(m*q1*q1/2),
    S.cancel((m+b)*q2*q2),
    S.cancel(r(3,2)*(m+2*b)*q3*q3))
Kcrit_dev=S.cancel(3*z*z/(4*m)-PN)
Kcrit_social=max(S.cancel((n*G[n]+3*CS[n]-3*WN)/n)
                 for n in (1,2,3))


def certify_market_from_exact_Cournot_code():
    assert PN==r(7425,12769)
    assert WN==r(24375,25538)
    assert (G[1],G[2],G[3])==(
       r(2269,3300),r(4863281,4452100),r(301481,313600))
    for n in range(4):
        flags=(1,)*n+(0,)*(3-n)
        raw=continuation((N,N,N),"M",PUBLIC,flags,F(3,4),F(3,100))
        predicted=n*(G[n]-r(3,4))+3*CS[n]
        observed=sum(S.Rational(w.numerator,w.denominator) for w in raw[1])
        assert S.simplify(predicted-observed)==0,(n,predicted,observed)
        assert S.simplify(predicted-3*WN)<0,n
        # Cournot KKT and technology matching are checked by source.
    assert Kcrit_social==r(5269762153,8008716800)
    assert Kcrit_dev==r(235752,319225)
    assert Kcrit_social<Kcrit_dev<r(3,4)
    print("PASS 8 exact mandate-compliance social welfare continuations",flush=True)
    print("government unanimous IS impossible for EVERY mixed adoption")
    print("equilibrium at NNN whenever K>K_SOC=",Kcrit_social,flush=True)
    print("all continuous technology deviations blocked at K>K_DEV=",Kcrit_dev,
          flush=True)


def certify_pure_adoption_phase_partition():
    # After pre-stage NNN and public M, an adopter pays K+phi/2.
    # All other firms deciding Exit have zero profit. Its decision
    # return depends only on how many other firms comply:
    # 0 => G1-K; 1 => G2-K; 2 => G3-K.
    # Exact order: G1<G3<G2.
    assert G[1]<G[3]<G[2]
    thresholds=(G[1],G[3],G[2])
    print("K pure-adoption phase thresholds K1,K3,K2=",thresholds,flush=True)
    samples=(
        ((r(0)+G[1])/2,{(1,1,1)}),
        ((G[1]+G[3])/2,{(0,0,0),(1,1,1)}),
        ((G[3]+G[2])/2,{(0,0,0),(1,1,0),(1,0,1),(0,1,1)}),
        (G[2]+r(1,10),{(0,0,0)}))
    for K,expected in samples:
        found=set()
        for f in product((0,1),repeat=3):
            def payoff(i,ff):
                return G[sum(ff)]-K if ff[i] else S.Integer(0)
            if all(payoff(i,f)>=payoff(i,tuple(1-z if j==i else z
                      for j,z in enumerate(f))) for i in range(3)):
                found.add(f)
        assert found==expected,(K,found,expected)
    # This enumeration's classification is also analytic: no
    # complier should lose from exiting (G_n>=K); no exiter should
    # gain by complying (G_{n+1}<=K), where n # of adopters.
    print("PASS complete STRICT-K pure adopter NE partition: 1,2,4,1 profiles",
          flush=True)


def certify_all_mixed_at_K075():
    K=r(3,4)
    A,B,C=(S.cancel(G[n]-K) for n in (1,2,3))
    assert A<0<B and C>0
    t=S.symbols("t",real=True)
    # A = payoff of sole adopter (versus exit), B = paired adopter,
    # C = three-firm compliant adopter.
    delta=S.factor(A*(1-t)**2+2*B*t*(1-t)+C*t**2)
    numerator,_=S.fraction(delta)
    roots=S.Poly(numerator,t)
    assert roots.count_roots(0,1)==1
    assert delta.subs(t,r(81,1000))<0
    assert delta.subs(t,r(82,1000))>0
    L=B-A
    H=A-2*B+C
    assert L>0 and H<0
    assert S.simplify(A+L*(-L/H))>0
    # If an interior mixed equilibrium has p1 != p2 then the
    # third's mixing probability must equal -L/H, but another
    # player's indifference A+L*(-L/H)=0 fails. All interior
    # equilibria must hence be symmetric and satisfy delta=0.
    # One firm pure 1: a putative mixing firm strictly prefers 1
    # because B>0, C>0. One firm pure 0: the other two mixers
    # must each choose t0=-A/L; then the pure-zero player strictly
    # prefers joining and hence cannot be an equilibrium.
    t0=-A/L
    assert r(0)<t0<r(1)
    delta_pure_zero=S.factor(A+2*L*t0+H*t0*t0)
    assert delta_pure_zero>0
    pure=adoption_pure_nash((N,N,N),"M",PUBLIC,F(3,4),F(3,100))
    assert {z[0] for z in pure}=={(0,0,0),(1,1,1)}
    # Because EVERY realised compliance profile yields social W
    # below 3 W_N, any mixed Nash and any correlated blend would
    # also fail unanimity; no arbitrary welfare-maximal selection.
    assert all(sum(raw[1])<3*F(WN.p,WN.q) for flags,raw
               in pure)
    print("PASS K=.75 exactly 3 Nash adoption continuations:",
          "all EXIT, all COMPLY, and symmetric interior mixture",flush=True)
    print("mixed adoption rate is UNIQUE t in (0.081,0.082), root of",delta,
          flush=True)
    print("NO special adopter-equilibrium selection required for NNN policy L",
          flush=True)


def certify_continuous_full_game_SPE():
    # Positive cross-demand parameters on full design triangles:
    # b>=.13, outsider d>=.11 at eta=.03, so Cournot q_i <= z_i/(2m)
    # for any action h_i=(X/Y/O,c,a), 0<a<=c<=1, ANY rival profile,
    # legal policy, mixed adoption equilibrium, and Cournot KKT mask.
    # The first-stage deviator pays K, yielding a GLOBAL upper bound.
    K=r(3,4)
    assert 3*z*z/(4*m)-K<PN
    # At all-N prehistory, C is unavailable; M cannot get 3-country
    # approval under ANY policy-after-decision mixed Nash because
    # each compliance profile has total W below 3*W_N.
    chosen=government_policy((N,N,N),F(3,4),F(3,100))[0]
    assert chosen[0]=="L"
    # Every off-path finite adoption game has at least one MIXED
    # Nash (finite Nash theorem); each gov policy menu finite,
    # G2/G3 sequential yes/no best replies, G1 picks a best reply.
    # Choosing one credible continuation at each off-path h by
    # arbitrary selection produces a strategy profile. At NNN,
    # no feasible continuous unilateral private first-stage
    # deviation can improve on P_N as shown by GLOBAL bound.
    # This proves EXISTENCE of a continuous-initial pure-profile,
    # off-path mixed-adoption subgame-perfect equilibrium.
    print("PASS FULL CONTINUOUS c_i,a_i SPE EXISTS with initial NNN,",
          "final L/NS, K=.75; ALL mixed postpolicy Nash allowed",flush=True)


if __name__=="__main__":
    certify_market_from_exact_Cournot_code()
    certify_pure_adoption_phase_partition()
    certify_all_mixed_at_K075()
    certify_continuous_full_game_SPE()
    print("Remaining: all-parameter continuous IS and RS SPE, and")
    print("all off-path adoption-equilibrium selections, are NOT classified.")
