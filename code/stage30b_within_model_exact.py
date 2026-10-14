#!/usr/bin/env python3
"""Additional unchanged-model results; exact rational sign certificates.

Reuses only the Stage30 rational Bernstein conversion and constants. Rebuilds
new targets from the 3x3 demand matrix. This is construction evidence, not a
second blind independent audit or a proof-assistant certificate.
"""
import json
from pathlib import Path
import sympy as s
import stage30_independent_exact_audit as audit

R=s.Rational
m,g,v,k,r,phi=audit.m,audit.gam,audit.v,audit.kap,audit.rho,audit.phi
PI,GI,WI=audit.PI,audit.GI,audit.WI
c,a,eta=s.symbols('c a eta')
t,u,w,h=s.symbols('t u w h')
out={'baseline':'d1d267cd8eaa349a06df7ff4cd102343d22f7ff5',
     'method':'exact rational matrix derivation and Bernstein signs',
     'certificates':[],'identities':{},'rational_examples':[]}
audit.results=out


def certify(expr,subs,variables,name,weak=False):
    n,d=audit.numden(expr)
    audit.bernstein(n.subs(subs),variables,name+'_numerator',weak)
    audit.bernstein(d.subs(subs),variables,name+'_denominator')


def private_total(H,z,stocks,name):
    A=H+m*s.eye(3);D=s.expand(A.det());Q=A.adjugate()*z
    # Twice D^2 times [3(PI-phi/2)-sum(private pre-K firm returns)].
    N=s.expand((6*PI-3*phi+phi*sum(ci**2+ai**2 for ci,ai in stocks))*D**2
               -6*m*(Q.T*Q)[0])
    audit.bernstein(N,(t,u,w,h),name,weak=True)
    # A nonzero polynomial with nonnegative Bernstein coefficients is strictly
    # positive on the open cube. Boundary strictness is checked separately.
    return N,D


def main():
    H=s.Matrix([[m,g+k*a-v*c,g-eta*a],
                [g+k*a-v*c,m,g-eta*a],[g-eta*a,g-eta*a,m]])
    z=s.Matrix([1+r*c,1+r*c,1]);q=(H+m*s.eye(3)).inv()*z
    x,y=s.cancel(q[0]),s.cancel(q[2]);cs=s.cancel((q.T*H*q)[0]/2)
    F=s.cancel(3*m*x*x-phi*(c*c+a*a)/2)
    KV=s.cancel(WI-3*m*y*y-cs)
    B=s.cancel(GI-3*m*x*x-cs-phi*(1-c*c)/2)
    box={eta:R('.10')+R('.04')*t,c:u,a:w}
    for label,expr in [('F_strictly_concave_a',-s.diff(F,a,2)),
                       ('F_a_positive_at_zero',s.diff(F,a).subs(a,0)),
                       ('outsider_quantity_increases_a',s.diff(y,a))]:
        certify(expr,box,(t,u,w),label)
    # At eta=.14,a=1 the outsider cross-effect is zero: y_c=0.
    certify(-s.diff(y,c),box,(t,u,w),
            'outsider_quantity_nonincreases_c',weak=True)
    certify(F.subs({c:1,a:0})-PI+phi/2,{},(t,),
            'zero_a_full_c_founder_participation')
    certify(R('.54')-KV.subs({c:1,a:0}),{},(t,),
            'zero_a_full_c_outsider_veto')
    # Whole maximal-coordination equilibrium family c=1,a in [0,a*(eta)].
    certify(R('.54')-KV,{eta:R('.10')+R('.04')*t,c:1,a:R('.61')*u},
            (t,u),'full_c_low_a_outsider_veto')
    lowbox={eta:R('.10')+R('.04')*t,c:u,a:R('.61')*w}
    W=s.cancel(2*F+3*m*y*y+3*cs)
    for label,expr in [('world_welfare_increases_c',s.diff(W,c)),
                       ('world_welfare_increases_a',s.diff(W,a))]:
        certify(expr,lowbox,(t,u,w),label)
    # Blanket F_ac>0 on the full box is false; preserve an exact witness.
    bad=s.cancel(s.diff(F,a,c).subs({c:1,a:0,eta:R('.10')}))
    assert bad<0
    out['rejected_blanket_F_ac_positive']={'c':'1','a':'0','eta':'1/10',
      'F_ac':str(bad),'float':float(bad),'status':'FALSE'}
    # The weaker statement needed to bound the optimum is true: a*(1,eta)>.30
    # and F_ac>0 for a in [.30,.61]. No change to model primitives.
    certify(s.diff(F,a).subs({c:1,a:R('.30')}),
            {eta:R('.10')+R('.04')*t},(t,),
            'full_c_private_a_marginal_positive_at_30')
    certify(s.diff(F,a,c),
            {eta:R('.10')+R('.04')*t,c:u,a:R('.30')+R('.31')*w},
            (t,u,w),'private_a_marginal_increases_c_above_30')
    certify(-s.diff(F,a).subs(a,R('.61')),
            {eta:R('.10')+R('.04')*t,c:u},(t,u),
            'private_a_marginal_negative_at_61')
    q_upper=(1+r)/(2*m)
    founder_lower=(1+r-2*(g+k)*q_upper)/(2*m)
    entrant_upper=(1+r-2*(g-v)*founder_lower)/(2*m)
    outsider_min=s.cancel(y.subs({c:1,a:0}))
    out['identities']['outsider_quantity_min']=str(outsider_min)
    out['identities']['outsider_profit_min']=str(3*m*outsider_min**2)
    out['identities']['entrant_quantity_upper']=str(entrant_upper)
    out['identities']['entrant_net_upper']=str(3*m*entrant_upper**2-R('.54'))
    out['identities']['no_private_entry_margin']=str(
        3*m*outsider_min**2-(3*m*entrant_upper**2-R('.54')))
    out['identities']['no_public_entry_margin']=str(
        3*m*outsider_min**2-(PI-R('.54')-phi/2))
    assert R(out['identities']['no_private_entry_margin'])>0
    assert R(out['identities']['no_public_entry_margin'])>0
    # These bounds apply to any symmetric incumbent pair, all legal entry:
    # entrant intercept <=1+rho*c, founders' intercept =1+rho*c.
    # The upper expression is increasing in c and maximized at c=1.
    entry_c=(1+r*c-2*(g-v)*(1+r*c-2*(g+k)*q_upper)/(2*m))/(2*m)
    out['identities']['entry_upper_increases_c']=str(s.diff(entry_c,c))
    assert s.diff(entry_c,c)>0
    # The same outsider minimum applies to any asymmetric remaining pair,
    # because its technologies are its two minima.
    out['identities']['public_equilibrium_welfare']='3*(WI-K), since all initial a=0'
    # Three-developer L candidate reductions: maxima in c and a must both tie.
    # Aligned: minimal c has minimal a; other firms tie both maxima.
    c1=t*u;c2=t;a1=c1*w;a2=a1+(c2-a1)*h
    H=s.Matrix([[m,g+k*a1-v*c1,g+k*a1-v*c1],
                [g+k*a1-v*c1,m,g+k*a2-v*c2],
                [g+k*a1-v*c1,g+k*a2-v*c2,m]])
    z=s.Matrix([1+r*c1,1+r*c2,1+r*c2])
    Na,Da=private_total(H,z,[(c1,a1),(c2,a2),(c2,a2)],'three_aligned_total_private_gap')
    # Crossed: minimal c is one of the maximum-a firms.
    a1=c1*w;a3=a1*h
    H=s.Matrix([[m,g+k*a1-v*c1,g+k*a3-v*c1],
                [g+k*a1-v*c1,m,g+k*a3-v*c2],
                [g+k*a3-v*c1,g+k*a3-v*c2,m]])
    Nc,Dc=private_total(H,z,[(c1,a1),(c2,a1),(c2,a3)],'three_crossed_total_private_gap')
    # Boundary equality proof: use t=1; positivity on faces with c1<1
    # or a>0 must not be inferred merely from an interior Bernstein sign.
    # Every term's coefficient is nonnegative in Bernstein representation;
    # enumerate all faces, including corners, and retain only identically-zero
    # restrictions for explicit economic interpretation in the proof document.
    out['three_private_zero_faces']={}
    import itertools
    for name,N in [('aligned',Na),('crossed',Nc)]:
        zeros=[]
        for face in itertools.product([None,R(0),R(1)],repeat=4):
            sub={var:value for var,value in zip((t,u,w,h),face) if value is not None}
            if s.expand(N.subs(sub))==0:
                zeros.append({str(key):str(value) for key,value in sub.items()})
        out['three_private_zero_faces'][name]=zeros
        assert zeros
        for face in zeros:
            assert face.get('t')=='1' and face.get('u')=='1' and face.get('w')=='0'
            if name=='aligned':assert face.get('h')=='0'
        required={'t':'1','u':'1','w':'0'}
        if name=='aligned':required['h']='0'
        assert required in zeros
    # Exact witnesses: low and high RS welfare under the same institution.
    for cc,aa,ee,kk in [(R(1),R(0),R('.14'),R('.55')),
                        (R(1),R('.5'),R('.14'),R('.55')),
                        (R('.95'),R(0),R('.14'),R('.55')),
                        (R('.929'),R(0),R('.14'),R('.54')),
                        (R('.929'),R(0),R('.14'),R('.55'))]:
        sub={c:cc,a:aa,eta:ee}
        entry={'c':str(cc),'a':str(aa),'eta':str(ee),'K':str(kk)}
        vals={'F_minus_public_private':F-PI+phi/2,'F_a':s.diff(F,a),
              'member_policy_gain':B,'outsider_policy_gain':KV-kk,
              'world_RS_minus_public':2*F+3*m*y*y+3*cs-3*WI+kk}
        for label,expr in vals.items():
            value=s.cancel(expr.subs(sub));entry[label]={'rational':str(value),'float':float(value)}
        out['rational_examples'].append(entry)
    Path('docs/audit/STAGE30B_EXACT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'certificates':len(out['certificates']),
                      'zero_faces':out['three_private_zero_faces'],
                      'examples':out['rational_examples']},indent=2))


if __name__=='__main__':main()
