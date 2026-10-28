#!/usr/bin/env python3
"""Finite checks of detector-capacity ingredients; not a proof of asymptotic coding."""
from __future__ import annotations
import argparse
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
TOL = 2e-10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(x, y, label: str, atol: float = TOL) -> None:
    require(bool(np.allclose(x, y, atol=atol, rtol=0)), label)


def entropy(p) -> float:
    p = np.asarray(p, dtype=float)
    require(float(np.min(p)) >= -TOL, 'Negative probability')
    q = p[p > 0]
    return float(-np.sum(q * np.log2(q)))


def von_neumann(rho) -> float:
    close(rho, rho.conj().T, 'Non-Hermitian state')
    return entropy(np.linalg.eigvalsh(rho))


def g(x: float) -> float:
    require(x >= 0 and math.isfinite(x), 'Invalid occupation')
    return 0.0 if x == 0 else (math.log1p(x) + x * math.log1p(1 / x)) / math.log(2)


def binomial(n: int, p: float) -> np.ndarray:
    require(n >= 0 and 0 <= p <= 1, 'Invalid binomial parameters')
    return np.array([math.comb(n, k) * p**k * (1-p)**(n-k) for k in range(n+1)])


def thin(p, q: float) -> np.ndarray:
    ans = np.zeros(len(p))
    for n, weight in enumerate(p):
        ans[:n+1] += weight * binomial(n, q)
    return ans


def counts(p, a: float, b: float):
    c = 1-a-b
    require(min(a, b, c) >= 0, 'Invalid splitter')
    d = len(p)
    bk, ek = np.zeros((d, d)), np.zeros((d, d))
    residual = 0.0
    for n, weight in enumerate(p):
        for j in range(n+1):
            for k in range(n-j+1):
                ell = n-j-k
                prob = weight * math.comb(n, j) * math.comb(n-j, k) * a**j * c**k * b**ell
                bk[j, k] += prob
                ek[ell, k] += prob
                if c > 0:
                    residual += prob * (j-a*k/c)**2
    return bk, ek, residual


def splitter(d: int, a: float, b: float) -> np.ndarray:
    c = 1-a-b
    v = np.zeros((d, d, d, d), dtype=complex)
    for n in range(d):
        for j in range(n+1):
            for ell in range(n-j+1):
                k = n-j-ell
                v[j, ell, k, n] = math.sqrt(math.comb(n,j)*math.comb(n-j,ell)*a**j*b**ell*c**k)
    return v.reshape(d**3, d)


def marginals(v, rho):
    d = rho.shape[0]
    joint = (v @ rho @ v.conj().T).reshape((d,)*6)
    bd = np.einsum('jlkJlK->jkJK', joint).reshape(d*d,d*d)
    ed = np.einsum('jlkjLK->lkLK', joint).reshape(d*d,d*d)
    return bd, ed


def attenuate_first(rho, t: float, d: int):
    out = np.zeros_like(rho)
    for ell in range(d):
        k = np.zeros((d,d),dtype=complex)
        for n in range(ell,d):
            k[n-ell,n] = math.sqrt(math.comb(n,ell)*(1-t)**ell*t**(n-ell))
        kk = np.kron(k,np.eye(d))
        out += kk @ rho @ kk.conj().T
    return out


def check_counts():
    rng = np.random.default_rng(20261028)
    cases = 0
    for d in (2,5,10,16):
        for a,b in ((.25,0),(.25,.1),(.6,.2),(.49,.48),(.8,.1)):
            p = rng.dirichlet(np.ones(d))
            mean = float(np.dot(np.arange(d),p))
            bk,ek,residual = counts(p,a,b)
            close(bk.sum(),1,'Count normalization')
            close(ek.sum(),1,'Complement normalization')
            close(bk.sum(axis=0),ek.sum(axis=0),'Duplicated flag')
            direct = entropy(bk.ravel())-entropy(ek.ravel())
            identity = entropy(thin(p,1-b))-entropy(thin(p,1-a))
            identity += sum(p[n]*(entropy(binomial(n,a))-entropy(binomial(n,b))) for n in range(d))
            close(direct,identity,'Thinning identity')
            c = 1-a-b
            close(residual,a*(a+c)*mean/c,'Residual second moment')
            ue = .5*math.log2(2*math.pi*math.e*(a*(a+c)*mean/c+1/12))
            require(direct <= ue+TOL,'Energy converse')
            if b:
                ub = math.log2((1-b)/(1-a))+.5*math.log2(2*math.pi*math.e*max(1/12,a*(1-a)/(b*(1-b))))
                require(direct <= ub+TOL,'Loss converse')
            for q in (.001,.1,.5,.9,1.):
                require(entropy(thin(p,q)) >= entropy(p)+math.log2(q)-TOL,'Thinning entropy gain')
            cases += 1
    # A rare large pulse: fixed mean, substantially larger second moment.
    p = np.zeros(401); p[0]=.995; p[400]=.005
    for q in (.01,.2,.7):
        require(entropy(thin(p,q)) >= entropy(p)+math.log2(q)-TOL,'Rare-pulse thinning')
    return {'diagonal_cases':cases,'rare_pulse_mean':2.0,'rare_pulse_second_moment':800.0}


def check_binomial():
    cases = 0
    for n in (0,1,2,3,5,10,30,100,256):
        for p in (0,1e-5,.001,.01,.1,.25,.5,.9,.99999,1):
            dist=binomial(n,p); v=n*p*(1-p)
            close(dist.sum(),1,'Binomial normalization')
            h=entropy(dist)
            require(h+TOL >= .5*math.log2(1+v),'Binomial entropy lower bound')
            require(h <= .5*math.log2(2*math.pi*math.e*(v+1/12))+TOL,'Binomial entropy upper bound')
            require(float(np.dot(dist,dist)) <= 1/math.sqrt(1+v)+TOL,'Collision bound')
            cases += 1
    return {'binomial_cases':cases}


def check_negative_binomial():
    cases=0
    for r in (1,2,3,10,40):
        for mu in (.05,.25,1.,10.):
            z=mu/(1+mu); prob=(1+mu)**(-r)
            mass=prob; collision=prob*prob; k=0
            while True:
                ratio=z*(k+r)/(k+1)
                nxt=prob*ratio
                if ratio<1 and nxt/(1-ratio)<1e-13:
                    tail_collision=nxt*nxt/(1-ratio*ratio)
                    break
                prob=nxt; k+=1
                mass+=prob; collision+=prob*prob
                require(k<100000,'Negative-binomial tail did not converge')
            close(mass,1,'Negative-binomial mass',atol=2e-12)
            w=mu*(1+mu)
            bound=math.pi/(4*math.sqrt(r*w))
            require(collision+tail_collision<=bound+TOL,'Negative-binomial collision bound')
            cases+=1
    return {'negative_binomial_cases':cases}


def check_quantum():
    rng=np.random.default_rng(19052005)
    results=[]
    for d,a,b,energy in ((3,.25,0.,2.),(4,.25,.1,2.),(4,.7,.1,10.)):
        v=splitter(d,a,b)
        close(v.conj().T@v,np.eye(d),'Isometry')
        z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        rho=z@z.conj().T;rho/=np.trace(rho)
        bd,ed=marginals(v,rho)
        close(attenuate_first(bd,b/a,d),ed,'Joint degradation including helper correlations')
        thermal=np.array([(energy/(1+energy))**n for n in range(d)]);thermal/=thermal.sum()
        bd,ed=marginals(v,np.diag(thermal))
        rb=bd.reshape(d,d,d,d);re=ed.reshape(d,d,d,d)
        bstate=np.einsum('jkjk->',rb) # only a normalization check
        close(bstate,1,'Thermal state normalization')
        bm=np.einsum('jkJk->jJ',rb)
        em=np.einsum('lkLk->lL',re)
        collision_prediction=float(np.trace(bm@bm).real+np.trace(bd@bd).real)
        collision_prediction-=sum(float(np.trace(rb[:,k,:,k]@rb[:,k,:,k]).real) for k in range(d))
        effects=np.zeros((d,d),complex)
        purities=[];infos=[]
        for phases in itertools.product((1,1j,-1,-1j),repeat=d):
            w=np.array(phases,dtype=complex)
            effects+=np.outer(w,w.conj())/(4**d)
            sb=np.einsum('k,l,jkJl->jJ',w.conj(),w,rb)
            se=np.einsum('k,l,jkJl->jJ',w.conj(),w,re)
            close(np.trace(sb),1,'Outcome probability')
            close(np.trace(se),1,'Complement outcome probability')
            purities.append(float(np.trace(sb@sb).real))
            infos.append(von_neumann(sb)-von_neumann(se))
        close(effects,np.eye(d),'POVM completeness')
        close(np.mean(purities),collision_prediction,'Exact phase collision identity')
        bound=-math.log2(float(np.trace(bm@bm).real+np.trace(bd@bd).real))-von_neumann(em)
        require(float(np.mean(infos))+TOL >= bound,'Coherent information bound')
        results.append({'cutoff_dimension':d,'receiver':a,'inaccessible':b,'outcomes':4**d,
                        'mean_coherent_information':round(float(np.mean(infos)),10),
                        'purity_lower_bound':round(bound,10)})
    return results


# Rational interval arithmetic. No floating-point premise enters the displayed certificate.
def iadd(x,y):return x[0]+y[0],x[1]+y[1]
def ineg(x):return -x[1],-x[0]
def isub(x,y):return iadd(x,ineg(y))
def imul(x,y):
    p=[a*b for a in x for b in y];return min(p),max(p)
def idiv(x,y):
    require(y[0]>0,'Interval divisor not positive')
    return imul(x,(1/y[1],1/y[0]))
def scale(x,a):return imul(x,(F(a),F(a)))


def log_reduced(x: F, terms: int=48):
    require(1 <= x <= 2,'Log range reduction')
    t=(x-1)/(x+1)
    s=sum((2*t**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    rem=2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return s,s+rem


LN2=log_reduced(F(2))
def ln_interval(x: F):
    require(x>0,'Log argument not positive')
    k=0
    while x<1:x*=2;k-=1
    while x>2:x/=2;k+=1
    return iadd(log_reduced(x),scale(LN2,k))
def log2_interval(x: F):return idiv(ln_interval(x),LN2)
def g_interval(x: F):
    if x==0:return F(0),F(0)
    return isub(scale(log2_interval(x+1),x+1),scale(log2_interval(x),x))


def certificate():
    a,b,energy=F(1,4),F(1,10000),F(1000000)
    purity=1/(1+2*a*energy)+1/(1+2*(1-b)*energy)
    local=isub(ineg(log2_interval(purity)),g_interval(b*energy))
    ratio=max(F(1,12),a*(1-a)/(b*(1-b)))
    # pi < 22/7 makes this a valid (slightly relaxed) upper bound.
    count=iadd(log2_interval((1-b)/(1-a)),scale(iadd(log2_interval(2*F(22,7)*ratio),idiv((F(1),F(1)),LN2)),F(1,2)))
    coll=isub(g_interval(a*energy),g_interval(b*energy))
    require(local[0]>F(1051,100) and local[1]<F(1052,100),'Coherent rate enclosure')
    require(count[1]<F(79,10),'Counting rate upper certificate')
    require(coll[0]>F(1128,100) and coll[1]<F(1129,100),'Collective rate enclosure')
    require(local[0]-count[1]>F(261,100),'Strict detector separation certificate')
    return {'receiver_fraction':'1/4','inaccessible_fraction':'1/10000','mean_photons':1000000,
            'coherent_lower_interval':[10.51,10.52], 'counting_capacity_less_than':7.9,
            'collective_capacity_interval':[11.28,11.29], 'certified_separation_greater_than':2.61,
            'method':'48-term rational atanh logarithms; pi < 22/7; no float comparison premise'}


def check_scalar_bounds():
    cases=0
    for a in (.01,.1,.25,.6,.95):
        for fraction in (0,.01,.1,.5,.99):
            b=min(a,1-a)*fraction
            for energy in (0,1e-6,.1,1,10,1e3,1e6):
                coll=g(a*energy)-g(b*energy)
                lower=max(0,-math.log2(1/(1+2*a*energy)+1/(1+2*(1-b)*energy))-g(b*energy))
                require(lower<=coll+TOL,'Local lower exceeds collective capacity')
                require(coll-lower<=math.log2(math.e)+TOL,'Constant-gap implication')
                cases+=1
    return {'scalar_parameter_cases':cases}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,help='Write a separate generated JSON; never overwrite the reference.')
    args=parser.parse_args()
    result={'counting':check_counts(),'binomial':check_binomial(),'coherent_measurements':check_quantum(),
            'negative_binomial':check_negative_binomial(),'scalar_bounds':check_scalar_bounds(),'finite_energy_certificate':certificate()}
    reference=ROOT/'verification'/'expected.json'
    require(reference.is_file(),'Missing committed expected.json')
    require(json.loads(reference.read_text())==result,'Results differ from the committed reference')
    if args.output:
        require(args.output.resolve()!=reference.resolve(),'Refusing to overwrite expected.json')
        require(not args.output.exists(),'Refusing to overwrite an existing output')
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('All finite checks passed. General capacity and asymptotic results require the written proofs.')


if __name__=='__main__':main()
