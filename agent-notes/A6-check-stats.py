# A6 audit, 2026-11-02: recomputes sinc order vs 0.262 fDR, Bonett n, Wilson CI, LoA/SEM precision and A5 sample sizes. Needs numpy+scipy.
import numpy as np
from math import sqrt
from scipy import stats
fmod=128000.
def sincN(f,fdr,n):
    N=fmod/fdr; x=np.pi*f/fmod
    return np.abs(np.sin(N*x)/(N*np.sin(x)))**n
for n in [1,2,3,4,5]:
    f=np.linspace(0.1,250,250000); g=20*np.log10(sincN(f,500,n))
    print("sinc order",n,"-3dB/fDR", f[np.argmin(abs(g+3))]/500)
# Bonett
z=1.959964
def bon(r,k,w): return 8*z**2*(1-r)**2*(1+(k-1)*r)**2/(k*(k-1)*w**2)+1
print("Bonett example",bon(.85,4,.2))
for r,k,w in [(.85,2,.2),(.85,3,.2),(.85,2,.15),(.75,2,.2),(.9,2,.1)]: print(r,k,w,round(bon(r,k,w),1))
# Wilson 27/30
def wilson(x,n,z=1.959964):
    p=x/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*sqrt(p*(1-p)/n+z*z/(4*n*n))/d; return c-h,c+h
for x,n in [(27,30),(18,20),(9,10)]: print("wilson",x,n,wilson(x,n), "exact", stats.beta.ppf(.025,x,n-x+1), stats.beta.ppf(.975,x+1,n-x))
# design effect: suppose 1 subject 30 sets ICC within? effective n
# LoA CI halfwidth
for n in [15,30,60,100]: print("LoA CI hw",n, stats.t.ppf(.975,n-1)*sqrt(3/n)*5)
# SEM chi2 bounds
for n in [15,30,60]:
    lo=sqrt(n/stats.chi2.ppf(.975,n)); hi=sqrt(n/stats.chi2.ppf(.025,n)); print("SEM ratio",n,round(lo,2),round(hi,2), "11Hz upper",round(11*hi,1))
# sensitivity example
p=.85;d=.07; print("n pos",z*z*p*(1-p)/d**2)
# RCT
d=.3; n=2*(1.959964+0.841621)**2/d**2; print("RCT per group",n, n*(1-.64))
