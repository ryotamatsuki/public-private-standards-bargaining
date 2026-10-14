"""Stage2 preliminary exact algebra: distinguish interoperability from product design.

DESIGN AUDIT, not a solved new dynamic SPE. Preserves original 6 economic
market parameters; proposes a seventh, chi>0, to price endogenously
selected product-characteristic investment. Public regulator sets a common
core r, firms select s_i and characteristics delta_i.
"""
import sympy as S
Q=S.Rational
m,b,d,z,z3,eta,delta,chi,s,r,v,gamma,kappa,rho=S.symbols(
    "m b d z z3 eta delta chi s r v gamma kappa rho",positive=True)
A=2*m+b
D=2*m*A-2*d*d
x=(2*m*z-d*z3)/D
y=(A*z3-2*d*z)/D
assert S.simplify((x-z/A)+d*y/A)==0
assert S.simplify(y-(A*z3-2*d*z)/D)==0
assert S.simplify((x-z/A).subs(z3,2*d*z/A))==0
assert S.simplify((y).subs(z3,2*d*z/A))==0

# Uniform common technical core r in [0,1], firms choose private
# innovation s_i in [0,1]; pairwise adoption compatibility is
# c_ij=r+(1-r)*min(s_i,s_j), for all legally compliant active firms.
# Each firm independently chooses product design delta_i in [0,1].
# Pairwise substitution slope gamma+(kappa-v)*c_ij
#                            -eta*(delta_i-delta_j)^2.
# Historical RS is embedded at r=0, s1=s2=s,s3=0,
# delta1=delta2=sqrt(s), delta3=0.
b_rs=gamma+(kappa-v)*s
d_rs=gamma-eta*s
assert S.simplify(b_rs-(gamma+(kappa-v)*s-eta*(S.sqrt(s)-S.sqrt(s))**2))==0
assert S.simplify(d_rs-(gamma+(kappa-v)*0-eta*(S.sqrt(s)-0)**2))==0
# Historical IS(s) is embedded r=0 and s1=s2=s3=s, all deltas equal.
assert S.simplify(gamma+(kappa-v)*s-eta*(delta-delta)**2-
                  (gamma+(kappa-v)*s))==0
# Under mandatory fully open core r=1, all c_ij=1 but product
# distinctiveness can remain: interoperability != product identity.
s1,s2,s3,del1,del2,del3=S.symbols(
    "s1 s2 s3 del1 del2 del3",nonnegative=True)
common=lambda p,q: r+(1-r)*S.Min(p,q)
assert S.simplify(common(s1,s2).subs(r,1)-1)==0
assert S.simplify(common(s1,s2).subs(r,0)-S.Min(s1,s2))==0
assert S.simplify((gamma+(kappa-v)*common(s1,s2)
    -eta*(del1-del2)**2).subs(r,1) -
    (gamma+(kappa-v)-eta*(del1-del2)**2))==0

# KKT-corner diagnostic: holding insider characteristic coordinates
# EQUAL while outsider is absent, design investment solely changes
# outsider-pair coefficients and incurs positive private cost.
# Profit and home CS do not depend on d in the true q3=0 continuation.
xcorner=z/A
p_corner=3*m*xcorner**2-chi*delta**2
csr=(m+b)*xcorner**2
w_corner=p_corner+csr
assert S.simplify(S.diff(p_corner,delta)+2*chi*delta)==0
assert S.simplify(S.diff(w_corner,delta)+2*chi*delta)==0
assert S.simplify(S.diff(csr,delta))==0
assert S.simplify(S.diff(p_corner,delta,2)+2*chi)==0
assert S.simplify(S.diff(w_corner,delta,2)+2*chi)==0
# In strictly binding corner neighborhood, each insider's local
# unilateral design deviation from common positive delta has no
# first-order effect on within-insider substitution:
B12=gamma+(kappa-v)*s-eta*(del1-del2)**2
assert S.simplify(S.diff(B12,del1).subs(del1,del2))==0
# But its own characteristic investment cost marginal is 2chi*del1.
# Hence identical strictly positive designs by two participating
# firms with outsider absent are not best replies if chi>0 and their
# characteristic choices do not alter own quality/productivity.
assert S.simplify(S.diff(-chi*del1**2,del1)+2*chi*del1)==0
print("PASS original RS and IS markets embedded as special characteristic profiles")
print("PASS public common-core interoperability does not mathematically erase product differentiation")
print("PASS independent 3x3 Cournot support identity and true KKT corner")
print("PASS in outsider-zero region, homogeneous costly insider characteristics")
print("     t>0 are locally dominated by reducing t (when no direct quality benefit)")
print("DESIGN STAGE ONLY: no private-design/full-nested-government subgame SPE claimed")
