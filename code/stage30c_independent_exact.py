#!/usr/bin/env python3
"""Exact Stage30C audit: matrix bounds, interval Horner and Sturm, no old imports."""
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
import sympy as s
from stage30c_independent_symbols import objects

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/audit/STAGE30C_EXACT_RESULTS.json'


def pack(q):
    q=Q(q)
    return {'rational':str(q),'float':float(q)}


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q
    def __add__(self,b): return Interval(self.lo+b.lo,self.hi+b.hi)
    def __mul__(self,b):
        t=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return Interval(min(t),max(t))


def horner_tree(terms,dim):
    if dim==0: return next(iter(terms.values()),Q(0))
    groups={}
    for expo,v in terms.items():
        groups.setdefault(expo[0],{})[expo[1:]]=v
    return {i:horner_tree(v,dim-1) for i,v in groups.items()}


def evaluate(tree,box):
    if isinstance(tree,Q): return Interval(tree,tree)
    if not tree: return Interval(Q(0),Q(0))
    z=Interval(Q(0),Q(0)); x=Interval(*box[0])
    for k in range(max(tree),-1,-1):
        z=z*x+evaluate(tree.get(k,Q(0)),box[1:])
    return z


def int_terms(poly):
    scale=s.ilcm(*[t.q for t in poly.coeffs()])
    return {e:Q(int(v*scale)) for e,v in poly.terms()},int(scale)


def certify_polynomial(poly,box,max_nodes=40000,max_depth=28):
    """Cover a box using rational ranges and derivative-certified minimum faces."""
    terms,scale=int_terms(poly); n=len(box)
    tree=horner_tree(terms,n)
    gradients=[]
    for axis in range(n):
        d={}
        for e,v in terms.items():
            if e[axis]:
                f=list(e);f[axis]-=1
                d[tuple(f)]=v*e[axis]
        gradients.append(horner_tree(d,n))
    widths=[hi-lo for lo,hi in box]
    leaves=[];visited=0;deepest=0
    def visit(original,depth):
        nonlocal visited,deepest
        visited+=1;deepest=max(deepest,depth)
        if visited>max_nodes or depth>max_depth:
            raise RuntimeError('UNRESOLVED: exact interval cover exhausted budget')
        current=list(original);reductions=[]
        rng=evaluate(tree,current)
        if rng.lo<=0:
            for axis in range(n):
                if current[axis][0]==current[axis][1]: continue
                der=evaluate(gradients[axis],current)
                if der.lo>=0: end=current[axis][0]
                elif der.hi<=0: end=current[axis][1]
                else: continue
                reductions.append((axis,str(der.lo),str(der.hi),str(end)))
                current[axis]=(end,end)
            rng=evaluate(tree,current)
        if rng.lo>0:
            leaf={'box':[[str(t) for t in b] for b in original],
                  'minimum_faces':reductions,'lower':str(rng.lo)}
            leaves.append(leaf);return {'leaf':len(leaves)-1}
        ratios=[(b[1]-b[0])/w if w else Q(0) for b,w in zip(current,widths)]
        axis=max(range(n),key=ratios.__getitem__)
        if not ratios[axis]:
            raise RuntimeError('FAILED: nonpositive exact point '+str(current))
        mid=sum(current[axis])/2
        left=list(current);right=list(current)
        left[axis]=(current[axis][0],mid);right[axis]=(mid,current[axis][1])
        return {'box':[[str(t) for t in b] for b in original],
                'minimum_faces':reductions,'axis':axis,
                'left':visit(left,depth+1),'right':visit(right,depth+1)}
    proof=visit(list(box),0)
    # Recheck the stored proof, including cover and derivative directions.
    def verify(node,expected):
        if 'leaf' in node:
            node=leaves[node['leaf']];child=None
        else: child=node
        assert [[str(t) for t in b] for b in expected]==node['box']
        current=list(expected)
        for axis,lo,hi,end in node['minimum_faces']:
            der=evaluate(gradients[axis],current)
            assert (str(der.lo),str(der.hi))==(lo,hi)
            end=Q(end)
            assert ((der.lo>=0 and end==current[axis][0]) or
                    (der.hi<=0 and end==current[axis][1]))
            current[axis]=(end,end)
        if child is None:
            actual=evaluate(tree,current).lo
            assert actual==Q(node['lower']) and actual>0
        else:
            axis=child['axis'];mid=sum(current[axis])/2
            assert current[axis][0]<mid<current[axis][1]
            left=list(current);right=list(current)
            left[axis]=(current[axis][0],mid);right[axis]=(mid,current[axis][1])
            verify(child['left'],left);verify(child['right'],right)
    verify(proof,list(box))
    return {'method':'exact rational Horner / derivative minimum faces / dyadic cover',
            'scale':scale,'domain':[[str(t) for t in b] for b in box],
            'variables':[str(v) for v in poly.gens],
            'polynomial':str(poly.as_expr()),'degree':poly.degree_list(),
            'term_count':len(terms),'visited':visited,'leaf_count':len(leaves),
            'maximum_depth':deepest,'minimum_leaf_lower':str(min(Q(l['lower']) for l in leaves)),
            'leaves':leaves,'cover':proof,'rechecked':True}


def signed_rational_certificate(expr,vars,box,D):
    for power in range(1,7):
        cleared=s.cancel(expr*D**power)
        if cleared.is_polynomial(*vars): break
    else: raise RuntimeError('UNRESOLVED: denominator mapping')
    poly=s.Poly(cleared,*vars)
    assert s.cancel(expr-poly.as_expr()/D**power)==0
    cert=certify_polynomial(poly,box)
    cert['positive_denominator']='D**'+str(power)
    cert['primitive_identity_checked']=True
    return cert


def scalar_bounds():
    m,g,v,k,rho,phi=map(Q,['.99','.14','.01','.02','.32','.14'])
    h=Q(4,25);qu=(1+rho)/(2*m)
    r=h/m
    q_initial_lower=(1-r/(1-r)*(1+rho))/(2*m)
    ql=(1-2*h*qu)/(2*m)
    wl=(ql-r/(1-r)*qu)/(2*m)
    Dlo=2*m*(2*m+g-v)-2*g*g
    aa_upper=6*m*(Q(7,50)/Dlo)**2+24*m*Q(7,50)**2*qu**2/Dlo-phi
    # At a=.61, the concave x-quadratic is increasing up to the upper bound.
    am=Q(61,100);dmin=g-Q(7,50)*am;dmax=g-Q(1,10)*am
    bmin=g+k*am-v
    da_min=min(2*m*k+4*e*(g-e*am) for e in [Q(1,10),Q(7,50)])
    dlo=2*m*(2*m+bmin)-2*dmax*dmax
    xu=(1+rho-dmin*ql)/(2*m+bmin)
    fa61_upper=6*m*xu*(Q(7,50)-xu*da_min)/dlo-phi*am
    # Uniform entrant upper envelope is a convex quadratic in own capacity.
    e0=1-2*g*ql;e1=rho+2*v*ql
    E=lambda t:3*m*((e0+e1*t)/(2*m))**2-phi*t*t/2-Q(27,50)
    entrant_upper=max(E(Q(0)),E(Q(1)))
    c=Q(1);b=g-v;d=g;z=1+rho
    D=2*m*(2*m+b)-2*d*d;y=(2*m+b-2*d*z)/D
    outsider_lower=3*m*y*y
    qi=(1+rho)/(2*(m+g-v))
    P=3*m*qi*qi-phi/2
    qn=1/(2*(m+g));qprime=(rho*(m+g)+v)/(2*(m+g)**2)
    ac=Q(9,2)*m+3*(g-v)
    symmetric_net_deriv=2*ac*qn*qprime-3*v*qu**2-phi
    vals=dict(q_initial_lower=q_initial_lower,q_lower=ql,q_upper=qu,
        inverse_times_q_lower=wl,
        three_capacity_pair_margin=12*m*rho*wl-2*phi,
        three_capacity_bottom_margin=6*m*rho*wl-phi,
        home_policy_t_y_coefficient=m*ql-2*h*qu-h*h/m*qu,
        bottom_quantity_t_rhs=rho-h*v/m*qu,
        symmetric_national_net_derivative=symmetric_net_deriv,
        F_c_lower=6*m*ql*rho/(2*m+h)-phi,
        x_a_numerator_lower=Q(1,10)-qu*(2*m*k+4*Q(7,50)*g),
        F_aa_negative_margin=-aa_upper,
        F_a_at_061_negative_margin=-fa61_upper,
        Fa61_x_quadratic_increasing_margin=Q(7,50)-2*xu*da_min,
        entrant_envelope_convexity=3*e1*e1/(4*m)-phi/2,
        entry_to_private_gap=outsider_lower-entrant_upper,
        entry_to_public_gap=outsider_lower-(P-Q(27,50)),
        outsider_profit_lower=outsider_lower,entrant_net_upper=entrant_upper,
        compliance_vs_exit_margin=3/(4*m)-Q(14,25)-phi/2,
        world_T_c_margin=3*rho*(2*ql+2*m*wl)-2*phi)
    assert all(v>0 for v in vals.values()),vals
    return {k:pack(v) for k,v in vals.items()}


def main():
    o=objects();c,a,e=o['vars'];f=o['fields']
    D=2*o['m']*(2*o['m']+o['b'])-2*o['d']**2
    targets={
        'founder_policy_positive':(f['B'],[(Q(0),Q(1)),(Q(0),Q(61,100)),(Q(1,10),Q(7,50))]),
        'world_T_a_positive':(f['T_a'],[(Q(0),Q(1)),(Q(0),Q(61,100)),(Q(1,10),Q(7,50))]),
        'F_ac_positive_above_030':(f['F_ac'],[(Q(0),Q(1)),(Q(3,10),Q(61,100)),(Q(1,10),Q(7,50))]),
        'canonical_veto_below_K_min':(s.Rational(27,50)-f['V'],[(Q(1),Q(1)),(Q(3,10),Q(61,100)),(Q(1,10),Q(7,50))])}
    results={'domain':'baseline five constants, eta=[.10,.14], K=[.54,.56]',
             'proof_assistant':'NOT IMPLEMENTED; preliminary target map only',
             'scalar_bounds':scalar_bounds(),'certificates':{}}
    print('Exact matrix/envelope bounds passed.',flush=True)
    for name,(expr,box) in targets.items():
        cert=signed_rational_certificate(expr,(c,a,e),box,D)
        results['certificates'][name]=cert
        print(name,cert['leaf_count'],'leaves',cert['maximum_depth'],'depth',flush=True)
    # A univariate Sturm check gives the lower canonical root enclosure.
    rootexpr=s.cancel(f['F_a'].subs({c:1,a:s.Rational(3,10)}))
    num,den=s.fraction(rootexpr)
    if den.subs(e,s.Rational(1,10))<0:num,den=-num,-den
    poly=s.Poly(num,e)
    count=int(poly.count_roots(s.Rational(1,10),s.Rational(7,50)))
    assert count==0 and num.subs(e,s.Rational(1,10))>0
    denominator_ratio=s.cancel(den/D.subs({c:1,a:s.Rational(3,10)})**3)
    assert not denominator_ratio.free_symbols and denominator_ratio>0
    results['canonical_root_sturm']={'polynomial':str(poly.as_expr()),
        'eta_interval':['1/10','7/50'],'root_count':count,
        'left_sign':'positive','denominator_positive_ratio':str(denominator_ratio),
        'denominator_primitive_mapping':'positive constant times D**3'}
    sparse=o['WI']-(3*o['m']+s.Rational(3,2)*(o['m']+2*o['g']))/(2*(o['m']+o['g']))**2-s.Rational(14,25)
    assert sparse>0
    base_private=s.cancel(f['F'].subs({c:1,a:0})-o['P'])
    assert base_private>0
    results['sparse_policy_margin']=pack(Q(sparse))
    results['canonical_F_minus_P_lower']=pack(Q(base_private))
    # Verify accounting directly, without using the corollary as an assumption.
    founder_profit=o['P']-f['F']-o['phi']*a*a/2
    assert s.cancel(f['B']-founder_profit-(o['csI']-f['C']))==0
    results['preference_identity_checked']=True
    results['ante_government_identity_checked']=bool(s.cancel(
        o['WI']-f['F']-f['C']-(f['B']+o['phi']*a*a/2))==0)
    assert results['ante_government_identity_checked']
    # Exact algebraic participation boundary: F(c,0)=P, K=.55, eta=.14.
    participation=s.cancel((f['F']-o['P']).subs({a:0,e:s.Rational(7,50)}))
    lo,hi=Q(0),Q(1)
    def val(expr,x):return Q(s.cancel(expr.subs(c,s.Rational(x.numerator,x.denominator))))
    assert val(participation,lo)<0<val(participation,hi)
    for _ in range(42):
        mid=(lo+hi)/2
        if val(participation,mid)<0:lo=mid
        else:hi=mid
    boundary_v=s.cancel((s.Rational(11,20)-f['V']).subs({a:0,e:s.Rational(7,50)}))
    bv=signed_rational_certificate(boundary_v,(c,a,e),
        [(lo,hi),(Q(0),Q(0)),(Q(7,50),Q(7,50))],
        D.subs({a:0,e:s.Rational(7,50)}))
    results['weak_participation_boundary']={'c_interval':[str(lo),str(hi)],
        'defining_equation':str(participation),'unique':'F_c strictly positive',
        'K':'11/20','eta':'7/50','a':'0',
        'outsider_strict_rejection_certificate':bv,
        'firm_mandate_preference':'exactly indifferent at the defining root'}
    witnesses=[]
    for cap,aa,et,K in [('1','0','.14','.55'),('1','.5','.14','.55'),('.929','0','.14','.54'),('.929','0','.14','.55')]:
        subs={c:s.Rational(cap),a:s.Rational(aa),e:s.Rational(et)};kv=s.Rational(K)
        row={'c':cap,'a':aa,'eta':et,'K':K}
        for name,val in [('F_minus_P',f['F']-o['P']),('F_a',f['F_a']),('B',f['B']),
                         ('K_minus_V',kv-f['V']),('private_minus_public_world',f['T']+kv-3*o['WI'])]:
            row[name]=pack(Q(s.cancel(val.subs(subs))))
        witnesses.append(row)
    results['exact_witnesses']=witnesses
    results['source_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
        [Path(__file__),Path(__file__).with_name('stage30c_independent_symbols.py')]}
    OUT.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print('Saved',OUT.name,OUT.stat().st_size,'bytes',flush=True)


if __name__=='__main__':main()
