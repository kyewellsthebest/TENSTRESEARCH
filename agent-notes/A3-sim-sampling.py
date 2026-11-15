import numpy as np
fmod=128000.0
def sinc3(f,fdr):
    N=fmod/fdr
    x=np.pi*f/fmod
    num=np.sin(N*x); den=N*np.sin(x)
    with np.errstate(invalid='ignore',divide='ignore'):
        h=np.where(np.abs(den)<1e-15,1.0,num/den)
    return np.abs(h)**3
# check -3 dB
for fdr in [125,250,500,1000,2000,4000,8000]:
    f=np.linspace(0.01,fdr/2,200001); g=20*np.log10(sinc3(f,fdr))
    f3=f[np.argmin(np.abs(g+3))]
    print(f"{fdr:5d} SPS  -3dB {f3:7.1f} Hz ({f3/fdr:.4f} fDR)  gain@90 {20*np.log10(sinc3(90,fdr)):6.2f} @120 {20*np.log10(sinc3(120,fdr)):6.2f} @200 {20*np.log10(sinc3(200,fdr)):6.2f} @250 {20*np.log10(sinc3(min(250,fdr/2),fdr)):6.2f} @450 {20*np.log10(sinc3(450,fdr)) if 450<fdr/2 else float('nan'):6.2f}")
# EMG PSD model (Shwedyk 1977 form), scaled to target MDF
def psd(f,s=1.0):
    fl,fh=60.0*s,120.0*s
    return fh**4*f**2/((f**2+fl**2)*(f**2+fh**2)**2)
F=np.linspace(0.1,6000,600000)
def mdf(f,p):
    c=np.cumsum(p); c/=c[-1]; return f[np.searchsorted(c,0.5)]
def hp(f,fc=20,n=4): return 1/(1+(fc/f)**(2*n))
# find scale for true MDF 120 and 90 (in 20-450 band after ideal BP)
def true_mdf(s):
    m=(F>=20)&(F<=450); return mdf(F[m],psd(F[m],s))
def brentq(fn,a,b):
    for _ in range(80):
        m=(a+b)/2
        if fn(a)*fn(m)<=0: b=m
        else: a=m
    return (a+b)/2
s120=brentq(lambda s:true_mdf(s)-120,0.3,3); s90=brentq(lambda s:true_mdf(s)-90,0.3,3)
print("scale",s120,s90, "full-band MDF", mdf(F,psd(F,s120)), mdf(F,psd(F,s90)))
def measured(s,fdr,hpf=True,bip=None):
    fo=np.linspace(0.1,fdr/2,20000); tot=np.zeros_like(fo)
    for k in range(0,40):
        for sign in ([1] if k==0 else [1,-1]):
            fa=k*fdr+sign*fo
            fa=np.abs(fa); fa[fa<0.1]=0.1
            p=psd(fa,s)*sinc3(fa,fdr)**2
            if bip: p=p*bip(fa)
            tot+=p
    if hpf: tot=tot*hp(fo)
    m=fo<=min(450,fdr/2)
    alias=None
    return mdf(fo[m],tot[m])
for fdr in [500,1000,2000,4000]:
    a=measured(s120,fdr); b=measured(s90,fdr)
    print(f"{fdr} SPS: measured MDF fresh {a:6.1f} fatigued {b:6.1f}  drop {100*(b-a)/a:6.1f}% (true -25.0%)")
# aliasing power fraction at 500 SPS
for fdr in [500,1000,2000]:
    fo=np.linspace(0.1,fdr/2,20000)
    inb=psd(fo,s120)*sinc3(fo,fdr)**2
    al=np.zeros_like(fo)
    for k in range(1,40):
        for sign in [1,-1]:
            fa=np.abs(k*fdr+sign*fo); al+=psd(fa,s120)*sinc3(fa,fdr)**2
    print(fdr,"aliased power fraction in output", al.sum()/(al.sum()+inb.sum()), "fraction of true EMG power above fDR/2", psd(F[F>fdr/2],s120).sum()/psd(F,s120).sum())
# bipolar spatial filter zeros
for d in [0.020,0.0254]:
    for v in [4.5,4.0,3.5,3.0]:
        print(f"IED {d*1000:.1f} mm CV {v} m/s first dip {v/d:.0f} Hz")
def bipf(d,v): return lambda f: np.sin(np.pi*f*d/v)**2
for d in [0.020,0.0254]:
    a=mdf(F,psd(F,s120)*bipf(d,4.0)(F)); b=mdf(F,psd(F,s90)*bipf(d,3.0)(F))
    print(f"IED {d*1000} idealised single-CV bipolar: MDF fresh(4 m/s) {a:.1f} fatigued(3 m/s) {b:.1f}")
