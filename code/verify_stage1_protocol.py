"""Stage 1 one-shot contract matching and differentiated Cournot benchmark."""
from dataclasses import dataclass
from itertools import combinations,product
import sympy as s

SQ="SQ"
@dataclass(frozen=True)
class Deal:
    name:str
    countries:tuple
    depth:int=0
    royalty:object=s.Integer(0)
    fixed:object=s.Integer(0)
    @property
    def signers(self):
        return frozenset("G"+str(i) for i in self.countries) | frozenset("F"+str(i) for i in self.countries)

def match(messages,menu):
    """Unanimous exact contract; no priority rule; outsiders have no veto."""
    wins=tuple(sorted(k for k,z in menu.items() if all(messages.get(h,SQ)==k for h in z.signers)))
    occupied=set()
    for k in wins:
        assert not (occupied & menu[k].signers)
        occupied.update(menu[k].signers)
    return wins

def market(n,deals):
    a=s.Integer(1);v=s.Rational(1,10);gamma=s.Rational(1,4);kappa=s.Rational(1,20)
    M=s.Matrix([[1-v if i==j else gamma for j in range(n)] for i in range(n)])
    for z in deals:
        for i,j in combinations(z.countries,2):
            M[i,j]=M[j,i]=gamma+kappa*z.depth-v
    assert M.is_positive_definite
    firm=[s.Integer(0)]*n;cs=[];quantities=[]
    for k in range(n):
        c=s.Matrix([0 if i==k else s.Rational(1,10) for i in range(n)])
        eff=s.Matrix(c)
        for z in deals:
            if z.royalty:
                assert len(z.countries)==2
                eff[z.countries[1]]+=z.royalty
        B=M+s.diag(*[M[i,i] for i in range(n)])
        q=B.inv()*(a*s.ones(n,1)-eff)
        assert all(qi>=0 for qi in q)
        p=a*s.ones(n,1)-M*q
        for i in range(n):
            assert s.factor(p[i]-eff[i]-M[i,i]*q[i])==0
            firm[i]+=s.factor((p[i]-eff[i])*q[i])
        rec=s.Integer(0)
        for z in deals:
            if z.royalty:
                rec+=z.royalty*q[z.countries[1]]
                firm[z.countries[0]]+=z.royalty*q[z.countries[1]]
        surplus=s.factor((q.T*M*q)[0]/2)
        cs.append(surplus);quantities.append(tuple(q))
        real=s.factor(a*sum(q)-(q.T*M*q)[0]/2-(c.T*q)[0])
        assert s.factor(surplus+sum((p[i]-eff[i])*q[i] for i in range(n))+rec-real)==0
    for z in deals:
        for i in z.countries:firm[i]-=z.fixed
    firm=tuple(map(s.factor,firm))
    gov=tuple(s.factor(cs[i]+firm[i]) for i in range(n))
    return gov,firm,tuple(quantities),M

def getpay(profile,menu,pay):
    z=match(profile,menu)
    assert len(z)<=1
    return pay[z[0] if z else SQ]

def pure_ne(profile,menu,pay,players):
    cur=getpay(profile,menu,pay)
    for i,h in enumerate(players):
        for a in [SQ,*menu]:
            b=dict(profile);b[h]=a
            if getpay(b,menu,pay)[i]>cur[i]:return False
    return True

def strong_block(profile,menu,pay,players):
    """Enumerates EVERY possible coalitional deviation for 4-player test."""
    cur=getpay(profile,menu,pay)
    for size in range(1,len(players)+1):
        for members in combinations(range(len(players)),size):
            for acts in product([SQ,*menu],repeat=size):
                b=dict(profile)
                for i,a in zip(members,acts):b[players[i]]=a
                newer=getpay(b,menu,pay)
                if all(newer[i]>cur[i] for i in members):
                    return (members,acts)
    return None

def test():
    tri={z.name:z for z in [Deal("12",(0,1)),Deal("13",(0,2)),Deal("23",(1,2))]}
    p={h:SQ for i in range(3) for h in ("G"+str(i),"F"+str(i))}
    for h in tri["12"].signers:p[h]="12"
    assert match(p,tri)==("12",)
    p["F0"]="13"
    assert match(p,tri)==()
    p["F0"]="12";p["F2"]="13";p["G2"]="13"
    assert match(p,tri)==("12",)
    disjoint={z.name:z for z in (Deal("12",(0,1)),Deal("34",(2,3)))}
    assert match({h:z.name for z in disjoint.values() for h in z.signers},disjoint)==("12","34")
    b=market(3,[])
    interface=market(3,[Deal("12",(0,1),0)])
    platform=market(3,[Deal("12",(0,1),1)])
    for i in (0,1):
        assert interface[0][i]>platform[0][i]>b[0][i]
        assert interface[1][i]>platform[1][i]>b[1][i]
    assert interface[0][2]<b[0][2] and interface[1][2]<b[1][2]
    assert platform[3].is_positive_definite
    costly=market(3,[Deal("12",(0,1),1,fixed=s.Rational(3,100))])
    assert costly[0][0]<b[0][0] and costly[1][0]<b[1][0]
    licensed=market(3,[Deal("12",(0,1),0,royalty=s.Rational(1,50))])
    assert licensed[2]!=interface[2]
    menu={z.name:z for z in (Deal("I",(0,1),0),Deal("P",(0,1),1))}
    players=("G0","F0","G1","F1")
    def v(x):return (x[0][0],x[1][0],x[0][1],x[1][1])
    pay={SQ:v(market(2,[])),"I":v(market(2,[menu["I"]])),"P":v(market(2,[menu["P"]]))}
    null={x:SQ for x in players}
    ie={x:"I" for x in players};pe={x:"P" for x in players}
    assert pure_ne(null,menu,pay,players) and pure_ne(ie,menu,pay,players) and pure_ne(pe,menu,pay,players)
    assert strong_block(null,menu,pay,players)
    assert strong_block(pe,menu,pay,players)
    assert strong_block(ie,menu,pay,players) is None
    num=sum(pure_ne(dict(zip(players,x)),menu,pay,players) for x in product([SQ,*menu],repeat=4))
    assert num==65
    print("PASS: one-shot conflict-free matches, outsiders, disjoint coalitions, royalty and K accounting")
    print("PASS: 2-country 81 profiles, 65 pure NE; all-SQ and platform strong-blocked in tested menu")
    print("PASS: 3-country exact Cournot, own-network singleton benefit, depth-dependent substitution")
    print("3-country interface govt gains:",*[str(interface[0][i]-b[0][i]) for i in range(3)])
    print("3-country interface firm gains:",*[str(interface[1][i]-b[1][i]) for i in range(3)])
    print("SCOPE: finite exogenous contract menu, binding implementation, no general CPNE/existence.")
if __name__=="__main__":test()
