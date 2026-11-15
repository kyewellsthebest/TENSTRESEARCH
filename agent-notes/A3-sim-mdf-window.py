import numpy as np
rng=np.random.default_rng(1)
def psd(f,s):
    fl,fh=60.0*s,120.0*s; f=np.maximum(f,1e-3)
    return fh**4*f**2/((f**2+fl**2)*(f**2+fh**2)**2)
def gen(n,fs,s):
    X=rng.standard_normal(n)+1j*rng.standard_normal(n)
    f=np.fft.fftfreq(n,1/fs); X*=np.sqrt(psd(np.abs(f),s))
    return np.real(np.fft.ifft(X))
def welch_mdf(x,fs,seg):
    nseg=int(seg*fs); step=nseg//2; w=np.hanning(nseg); P=0;k=0
    for i in range(0,len(x)-nseg+1,step):
        X=np.fft.rfft((x[i:i+nseg]-x[i:i+nseg].mean())*w); P=P+np.abs(X)**2;k+=1
    f=np.fft.rfftfreq(nseg,1/fs); m=(f>=20)&(f<=min(450,fs/2))
    c=np.cumsum(P[m]); return f[m][np.searchsorted(c,c[-1]/2)]
fs=2000; s120=1.2794
for T in [0.25,0.5,1.0,2.0]:
    vals=[welch_mdf(gen(int(T*fs),fs,s120),fs,min(0.125,T)) for _ in range(800)]
    vals=np.array(vals); print(f"window {T:4.2f}s  MDF mean {vals.mean():6.1f}  SD {vals.std():5.1f} Hz  CV {100*vals.std()/vals.mean():4.1f}%  95% range +/-{1.96*vals.std():.1f}")
