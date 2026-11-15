# A6 audit, 2026-11-02: sensitivity of A3 500-SPS MDF bias to spectral shape; truncation vs sinc3 droop vs inverse-sinc compensation; bipolar dip effect on RELATIVE MDF change.
import numpy as np
fmod=128000.
def sinc3(f,fdr):
    N=fmod/fdr; x=np.pi*f/fmod
    with np.errstate(all='ignore'):
        h=np.where(np.abs(np.sin(x))<1e-15,1.0,np.sin(N*x)/(N*np.sin(x)))
    return np.abs(h)**3
F=np.linspace(0.1,6000,600000)
def mdf(f,p): c=np.cumsum(p); c/=c[-1]; return f[np.searchsorted(c,0.5)]
def hp(f,fc=20,n=4): return 1/(1+(fc/f)**(2*n))
shapes={
 'shwedyk 60/120 (A3)':lambda f,s: (120*s)**4*f**2/((f**2+(60*s)**2)*(f**2+(120*s)**2)**2),
 'shwedyk 40/160':lambda f,s: (160*s)**4*f**2/((f**2+(40*s)**2)*(f**2+(160*s)**2)**2),
 'shwedyk 80/100':lambda f,s: (100*s)**4*f**2/((f**2+(80*s)**2)*(f**2+(100*s)**2)**2),
 'gaussian pk80 sd50':lambda f,s: np.exp(-0.5*((f-80*s)/(50*s))**2),
 'lognormal':lambda f,s: np.exp(-0.5*(np.log(np.maximum(f,1e-3)/(90*s))/0.6)**2)/np.maximum(f,1e-3),
}
def solve(fn,target):
    a,b=0.2,4
    for _ in range(70):
        m=(a+b)/2; band=(F>=20)&(F<=450)
        v=mdf(F[band],fn(F[band],m))
        if v>target: b=m
        else: a=m
    return (a+b)/2
def measured(fn,s,fdr,filt=True,comp=False,upper=None):
    fo=np.linspace(0.1,fdr/2,20000); tot=np.zeros_like(fo)
    for k in range(0,40):
        for sg in ([1] if k==0 else [1,-1]):
            fa=np.abs(k*fdr+sg*fo); fa[fa<0.1]=0.1
            tot+=fn(fa,s)*(sinc3(fa,fdr)**2 if filt else (1.0 if k==0 else 0.0))
    if comp: tot=tot/np.maximum(sinc3(fo,fdr)**2,1e-6)
    tot*=hp(fo)
    up=min(450,fdr/2) if upper is None else upper
    m=(fo>=0)&(fo<=up); return mdf(fo[m],tot[m])
print("shape | true(20-450) 120->90 | 500 raw | 500 ideal-trunc only | 500 sinc-comp | 2k raw | 2k raw capped 250")
for name,fn in shapes.items():
    s1=solve(fn,120); s0=solve(fn,90)
    out=[]
    for args in [(500,True,False,None),(500,False,False,None),(500,True,True,None),(2000,True,False,None),(2000,True,False,250)]:
        a=measured(fn,s1,args[0],args[1],args[2],args[3]); b=measured(fn,s0,args[0],args[1],args[2],args[3])
        out.append(f"{a:5.1f}->{b:5.1f} ({100*(b-a)/a:5.1f}%)")
    print(name,'|',' | '.join(out))
# bipolar dip effect on relative change, shwedyk A3
fn=shapes['shwedyk 60/120 (A3)']; s1=solve(fn,120); s0=solve(fn,90)
for d in [0.020,0.0254]:
    for v1,v0 in [(4.0,3.0),(4.0,4.0*90/120)]:
        b=lambda f,v: np.sin(np.pi*f*d/v)**2
        band=(F>=20)&(F<=450)
        a=mdf(F[band],fn(F[band],s1)*b(F[band],v1)); c=mdf(F[band],fn(F[band],s0)*b(F[band],v0))
        print(f"IED {d*1000} CV {v1}->{v0:.2f}: {a:.1f}->{c:.1f} ({100*(c-a)/a:.1f}%)")
band=(F>=20)&(F<=450); print("no dip:",mdf(F[band],fn(F[band],s1)),mdf(F[band],fn(F[band],s0)))
