"""Stage 5 INTEGRATED six-player standards game: full exact-rational pilot.

Continuous underlying ACTION SPACE: every F_i simultaneously chooses
N or (label in {X,Y,O}, c_i, a_i), 0<=a_i<=c_i<=1.
X/Y are incompatible proprietary protocols, O an OPEN public-license
protocol, and different labels are incompatible. This source tests a
RESTRICTED 3-design action menu: (.5,0),(1,0),(1,.6) per label.
Continuous-strategy SPE IS NOT CLAIMED.

Three national governments observe firms' choices. G1 proposes L
(laissez faire), C(r) certification of an already privately developed
OPEN reference r, or M mandate of a legally pre-existing public-domain
reference O(1,0). G2 then G3 approve/reject proposal; unanimous
approval required, otherwise L. Recognition C opens a VOLUNTARY
costly technology-migration window. A public M is enforceable but
each firm can comply with independent public-domain IP or legally EXIT.
No government can appropriate patents X/Y. Costs of initial development
are sunk at the policy stage, and additional migration costs are incurred
ONCE when changing to a different reference.

After C, firms SIMULTANEOUSLY decide migrate or retain. After M, firms
SIMULTANEOUSLY decide comply or exit. Pure adoption Nash equilibria
are all enumerated; for this illustrative branch, one is selected by
MAXIMUM SUM of national W, then total firm profit, then compliance.
This is an EXPLICIT equilibrium-selection rule, not a claim that all
subgame-perfect equilibria deliver these outcomes.

Final differentiated Cournot in 3 identical national markets is solved
EXACTLY using Fraction Gauss elimination and all 8 active KKT sets.
Original 6 technology coefficients unchanged; Stage2 separable real
cost phi*(c_i^2+a_i^2)/2 plus disclosed OPTIONAL setup K.
Pair technology uses min(c_i,c_j), min(a_i,a_j), cohort-specific
Ghosh-Morita outsider separation; no unsupported demand-matrix
extrapolation. Source six variables and s-diagonal original recovered
for uniform same-label standards, but an ASYMMETRIC extension for
different individual c_i,a_i is a new substantive assumption.

Main exact enumerations: 3^3 migration/compliance deviation tests,
10^3 independent firm proposals, 6 original actors, K=0, .5, .75.
Outcomes: at K=0 all equilibria have 3-firm compatibility but policies
L/C/M all appear; at K=.5 IS and bilateral RS coexist as separate
initial Nash/SPE outcomes; at K=.75 only NS survives. This is for the
RESTRICTED DESIGN MENU and specified continuation selection.
"""
from functools import lru_cache
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter

v,g,k,rho,phi=F(1,100),F(7,50),F(1,50),F(8,25),F(7,50)
m=1-v
DESIGNS=((F(1,2),F(0)),(F(1),F(0)),(F(1),F(3,5)))
N=('N',F(0),F(0))
ACTIONS=(N,)+tuple((lab,c,a) for lab in ('X','Y','O')
                    for c,a in DESIGNS)
PUBLIC=('O',F(1),F(0))
ALL_FLAGS=tuple(product((0,1),repeat=3))

def cost(act,K):
    label,c,a=act
    return F(0) if label=='N' else K+phi*(c*c+a*a)/2

def solve_linear(A,z):
    n=len(z)
    rows=[list(A[i])+[z[i]] for i in range(n)]
    for i in range(n):
        pivot=next((j for j in range(i,n) if rows[j][i]!=0),None)
        assert pivot is not None
        rows[i],rows[pivot]=rows[pivot],rows[i]
        for h in range(i+1,n):
            factor=rows[h][i]/rows[i][i]
            for j in range(i,n+1):
                rows[h][j]-=factor*rows[i][j]
    result=[F(0)]*n
    for i in reversed(range(n)):
        result[i]=(rows[i][n]-sum(rows[i][j]*result[j]
                    for j in range(i+1,n)))/rows[i][i]
    return result

@lru_cache(None)
def continuation(pre,policy,ref,flags,K,eta):
    """Return (private profits, government payoffs, output, CS, post labels).
    Exact ex ante fixed sunk cost + one fresh actual conversion cost.
    """
    initial=[cost(x,K) for x in pre]
    additional=[F(0)]*3
    post=list(pre)
    exits=set()
    if policy in ('C','M'):
        for i,accept in enumerate(flags):
            if accept:
                if post[i]!=ref:additional[i]=cost(ref,K)
                post[i]=ref
            elif policy=='M':
                exits.add(i)
    M=[[m if i==j else g for j in range(3)] for i in range(3)]
    intercept=[F(1)]*3
    for i,j in combinations(range(3),2):
        if (i not in exits and j not in exits and
            post[i][0]!='N' and post[i][0]==post[j][0]):
            common_c=min(post[i][1],post[j][1])
            common_a=min(post[i][2],post[j][2])
            M[i][j]=M[j][i]=g+k*common_a-v*common_c
            intercept[i]=max(intercept[i],1+rho*common_c)
            intercept[j]=max(intercept[j],1+rho*common_c)
    # Only a TWO-firm matched cluster has a single distinguishable
    # outsider. Keep same insider-vs-outsider cross effect as original.
    for label in ('X','Y','O'):
        group=[i for i in range(3)
               if i not in exits and post[i][0]==label]
        if len(group)==2:
            common_a=min(post[i][2] for i in group)
            outsider=next(i for i in range(3) if i not in group)
            if outsider not in exits:
                for i in group:
                    M[i][outsider]=M[outsider][i]=g-eta*common_a
    # Positive definiteness in TEST domain:
    # each |offdiag| <=.152; diag m=.99, strict Gershgorin.
    assert all(sum(abs(M[i][j]) for j in range(3) if i!=j)<m
               for i in range(3))
    valid=[]
    for mask in ALL_FLAGS:
        active=[i for i in range(3) if mask[i] and i not in exits]
        if any(mask[i] for i in exits):continue
        if active:
            L=[[M[i][j]+(m if i==j else 0) for j in active]
               for i in active]
            x=solve_linear(L,[intercept[i] for i in active])
            if any(xi<=0 for xi in x):continue
        else:x=[]
        q=[F(0)]*3
        for i,qi in zip(active,x):q[i]=qi
        if all(intercept[i]-sum(M[i][j]*q[j] for j in range(3))<=0
               for i in range(3) if i not in active and i not in exits):
            valid.append(q)
    assert len(valid)==1,(pre,policy,ref,flags,len(valid))
    q=valid[0]
    cs=sum(q[i]*M[i][j]*q[j] for i in range(3)
           for j in range(3))/2
    p=tuple(3*m*q[i]**2-initial[i]-additional[i] for i in range(3))
    w=tuple(x+cs for x in p)
    return p,w,tuple(q),cs,tuple(post)

@lru_cache(None)
def adoption_pure_nash(pre,policy,ref,K,eta):
    equilibria=[]
    for flags in ALL_FLAGS:
        outcome=continuation(pre,policy,ref,flags,K,eta)
        p=outcome[0]
        if all(p[i]>=continuation(
                pre,policy,ref,tuple(1-f if j==i else f
                    for j,f in enumerate(flags)),K,eta)[0][i]
               for i in range(3)):
            equilibria.append((flags,outcome))
    return tuple(equilibria)

def select_adoption(pre,policy,ref,K,eta):
    eq=adoption_pure_nash(pre,policy,ref,K,eta)
    # This defines one selected Nash continuation, not a
    # unique-Nash or all-SPE statement.
    if not eq:return None
    return max(eq,key=lambda z:(sum(z[1][1]),sum(z[1][0]),
                                sum(z[0]),z[0]))

@lru_cache(None)
def government_policy(pre,K,eta):
    base=continuation(pre,'L',None,(0,0,0),K,eta)
    options=[('L',None,(0,0,0),base)]
    for ref in sorted(set(x for x in pre if x[0]=='O')):
        chosen=select_adoption(pre,'C',ref,K,eta)
        if chosen is not None:
            options.append(('C',ref,*chosen))
    chosen=select_adoption(pre,'M',PUBLIC,K,eta)
    if chosen is not None:
        options.append(('M',PUBLIC,*chosen))
    # G2, G3 separately approve proposals only with strictly higher
    # national W than L; otherwise they vote NO (tie rule).
    feasible=[x for x in options if x[0]=='L' or
              all(x[3][1][i]>base[1][i] for i in (1,2))]
    # G1 maximizes own national W over policies accepted by G2,G3.
    # Exact ties favor lower intervention: L > C > M.
    ranks={'L':2,'C':1,'M':0}
    selected=max(feasible,key=lambda x:(x[3][1][0],ranks[x[0]]))
    return selected,tuple(options)

def firm_nash(K,eta):
    results=[]
    for profile in product(ACTIONS,repeat=3):
        chosen,_=government_policy(profile,K,eta)
        firm_payoffs=chosen[3][0]
        best=True
        for i in range(3):
            for alternative in ACTIONS:
                altered=tuple(alternative if j==i else profile[j]
                              for j in range(3))
                dev=government_policy(altered,K,eta)[0][3][0][i]
                if dev>firm_payoffs[i]:
                    best=False
                    break
            if not best:break
        if best:results.append((profile,chosen))
    return results

def final_type(profile,policy):
    if policy[0]=='M':
        entrants=[i for i,x in enumerate(policy[2]) if x]
        if len(entrants)==3:return 'IS'
        if len(entrants)==2:return 'RS'
        return 'NS'
    post=policy[3][4]
    groups=Counter(x[0] for x in post if x[0]!='N')
    size=max(groups.values(),default=0)
    return 'IS' if size==3 else 'RS' if size==2 else 'NS'

def report(K,eta,expected_n,expected_policies,expected_types):
    equilibria=firm_nash(K,eta)
    policies=Counter(x[0] for _,x in equilibria)
    types=Counter(final_type(p,x) for p,x in equilibria)
    assert len(equilibria)==expected_n,(K,eta,'count',len(equilibria))
    assert dict(policies)==expected_policies,(K,eta,'policies',policies)
    assert dict(types)==expected_types,(K,eta,'types',types)
    assert len(ACTIONS)==10
    print('EXACT 1000 private initial profiles; all 3 x 9 unilateral',
          'deviations checked per profile',flush=True)
    print('eta',eta,'K',K,'SPE count',len(equilibria),
          'government policy',policies,'final standard types',types,flush=True)
    return equilibria

def unrestricted_continuous_NNN_deviation_bound():
    """Analytical deviation proof for ALL continuous (c_i,a_i) from NNN.

    With nonnegative cross substitution, the Cournot FOC for any active
    firm gives q_i <= z_i/(2*m). Every possible government response
    still has z_i<=1+rho. A deviator investing c_i>0 pays K upfront,
    so final profit <=3*(1+rho)^2/(4*m)-K. Thus at sufficiently high K
    NONE of the INFINITELY MANY technology deviations can profit.
    This is a Stage1 Nash bound conditional on the public governance
    continuation, NOT a full continuous all-history SPE existence proof.
    """
    PN=3*m/(4*(m+g)**2)
    gross_limit=3*(1+rho)**2/(4*m)
    K_critical=gross_limit-PN
    assert gross_limit==F(33,25)
    assert PN==F(7425,12769)
    assert K_critical==F(235752,319225)
    assert K_critical<F(3,4)
    assert government_policy((N,N,N),F(3,4),F(3,100))[0][0]=='L'
    assert gross_limit-F(3,4)<PN
    print("PASS unrestricted continuous unilateral-deviation exclusion",
          "whenever K >=",K_critical,flush=True)


def check_provenance_and_specific_subgames():
    # Private actions ARE INDEPENDENT labels, c and a; no joint
    # proposer or multi-agent joint deviations at the firm stage.
    assert len(ACTIONS)==10
    assert len(set((x[1],x[2]) for x in ACTIONS if x[0]=='X'))==3
    assert all(F(0)<=x[2]<=x[1]<=1 for x in ACTIONS)
    assert m>2*(g+k)
    eta=F(3,100)
    def case(pre,K=F(0)):
        return government_policy(pre,K,eta)
    closed=('X',F(1),F(0))
    open_=('O',F(1),F(0))
    first=case((N,N,N))[0]
    assert first[0]=='M' and first[2]==(1,1,1)
    assert all(x>0 for x in first[3][0])
    assert first[3][2][0]>0
    second=case((open_,open_,N))[0]
    assert second[0]=='C'
    assert second[3][2][2]>0
    third=case((closed,closed,N))[0]
    assert third[0]=='L'
    assert third[3][2][2]>0 # outsider ACTIVE, not a member
    assert case((N,N,N),F(3,4))[0][0]=='L'
    # At closed pair, IS mandate is rejected because incumbent
    # regulator G2 does NOT gain after sunk retooling.
    no=continuation((closed,closed,N),'L',None,(0,0,0),F(0),eta)
    upgrade=select_adoption((closed,closed,N),'M',PUBLIC,F(0),eta)
    assert upgrade is not None
    assert no[1][0]>upgrade[1][1][0]
    assert no[1][1]>upgrade[1][1][1]
    print('PASS government policies L,C,M genuinely distinct in subgames')

if __name__=='__main__':
    check_provenance_and_specific_subgames()
    unrestricted_continuous_NNN_deviation_bound()
    report(F(0),F(3,100),10,{'M':1,'C':6,'L':3},{'IS':10})
    report(F(1,2),F(3,100),14,{'M':1,'L':13},
           {'IS':2,'RS':12})
    report(F(3,4),F(3,100),1,{'L':1},{'NS':1})
    print('PASS Stage5 ONE integrated six-player finite DESIGN MENU SPE')
    print('NOT PROVED for unlimited continuous (c_i,a_i) action sets;')
    print('veto/government agenda and post-certification equilibrium')
    print('selection are explicitly institutional assumptions.')
