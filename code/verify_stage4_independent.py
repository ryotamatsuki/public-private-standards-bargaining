"""Stage 4 independent direct Fraction payoff evaluator; NO SymPy and no solver reuse."""
from fractions import Fraction as F

params=dict(a=F(1),gamma=F(1,10),v=F(1,10),kappa=F(1,50),
            export_cost=F(3,20),royalty=F(1,25))

def gaussian(A,y):
    A=[list(row)+[target] for row,target in zip(A,y)]
    n=len(A)
    for j in range(n):
        pivot=next(i for i in range(j,n) if A[i][j]!=0)
        A[j],A[pivot]=A[pivot],A[j]
        div=A[j][j];A[j]=[x/div for x in A[j]]
        for i in range(n):
            if i==j:continue
            t=A[i][j];A[i]=[x-t*y for x,y in zip(A[i],A[j])]
    return [row[-1] for row in A]

def payoff(z,pp=params):
    a,g,v,k,c,r=(pp[name] for name in
                  ('a','gamma','v','kappa','export_cost','royalty'))
    M=[[F(1)-v if i==j else g for j in range(3)] for i in range(3)]
    if z is not None:
        (u,w),depth=z;M[u][w]=M[w][u]=g+k*depth-v
    B=[[M[i][j]+(M[i][i] if i==j else 0) for j in range(3)]
       for i in range(3)]
    pi=[F(0)]*3;CS=[F(0)]*3;out=[]
    for dest in range(3):
        real=[F(0) if i==dest else c for i in range(3)]
        effective=real[:]
        if z is not None:effective[z[0][1]]+=r
        q=gaussian(B,[a-c for c in effective])
        assert min(q)>0
        out.append(tuple(q))
        prices=[a-sum(M[i][j]*q[j] for j in range(3)) for i in range(3)]
        for i in range(3):pi[i]+=(prices[i]-effective[i])*q[i]
        royalty=F(0)
        if z is not None:
            royalty=r*q[z[0][1]]
            pi[z[0][0]]+=royalty
        CS[dest]=sum(q[i]*M[i][j]*q[j] for i in range(3)
                     for j in range(3))/2
        resources=a*sum(q)-CS[dest]-sum(real[i]*q[i] for i in range(3))
        assert CS[dest]+sum((prices[i]-effective[i])*q[i] for i in range(3))+royalty==resources
    return ({('G',i):CS[i]+pi[i] for i in range(3)}|
            {('F',i):pi[i] for i in range(3)}),out
