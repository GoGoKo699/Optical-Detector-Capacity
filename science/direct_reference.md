# Capacity with a reference of linear mean energy

[Model](model.md) · [Structured detector](coherent_measurements.md) · [Record resources](detector_resources.md) · [Uniform gate implementation](finite_reference.md)

A fresh finite phase reference with mean photon number of order the useful
signal energy suffices to retain the full leading communication rate. The
argument bounds the reference information left in the actual complementary
output. At fixed additive tolerances, no reference factor growing as the square
root of the logarithm of the signal energy is needed for this capacity bound.

Use the apparatus contract and conserving lift in the
[finite-reference construction](finite_reference.md#apparatus-contract).
The sine reference and shift lift are established constructions, attributed
there to Åberg and to Chiribella, Yang, and Renner. The entropy estimate below is
proved here from the discrete Laplacian and the thermal maximum-entropy
principle. It supplies a capacity-specific application of that machinery;
neither a new general reference construction nor a priority claim is needed.

## The actual channel and its reference output

Assume $`a>b\ge0`$, $`0<a<1`$, and mean signal budget $`E>0`$. Choose a
thermal average input of mean $`x\le E`$, normalized after restriction to
$`0,\ldots,d-1`$, where $`d\ge2`$. Its mean is $`x_d<x`$. Let $`q`$ be the
smallest odd prime at least $`d`$, put $`h=q-1`$, and choose the predetermined
setting $`s`$ of $`U=\mathcal F_qD_s`$ by the
[ideal fixed-setting construction](coherent_measurements.md#one-predetermined-fourier-measurement-suffices).

For each collected mode, supply a fresh independent sine reference of width
$`K\ge1`$,

```math
|\xi_K\rangle=
\sqrt{\frac2{K+1}}\sum_{\ell=0}^{K-1}
\sin\!\left(\frac{\pi(\ell+1)}{K+1}\right)|h+\ell\rangle_W.
```

The conserving lift applies

```math
|k\rangle_D|n\rangle_W
\longmapsto
\sum_{j=0}^{q-1}U_{jk}|j\rangle_D|n+k-j\rangle_W
```

on the occupied sectors. The margins and sector completions specified in the
finite-reference construction make this a unitary on a bounded-below ladder.
Write $`T_v\xi_K`$ for the translated vector whenever its support remains
nonnegative. All translations used below satisfy that condition.

Let $`p_k`$ be the number distribution of the helper marginal before control;
it is diagonal and supported on $`0,\ldots,d-1`$. Flat Fourier matrix entries
give an exact uniform count distribution and the conditional reference state

```math
\Pr(Y=j)=\frac1q,\qquad
\rho_{W|j}=\sum_{k=0}^{d-1}p_k
|T_{k-j}\xi_K\rangle\langle T_{k-j}\xi_K|,
\qquad 0\le j<q.
```

Each state on the right has support in an interval of
$`J=K+d-1`$ consecutive reference levels. Its location depends on $`j`$;
its length and its entropy estimates do not. An outside outcome may be retained
in the detector alphabet; it has zero probability on this code support.

## Entropy of a mixture of translated sine references

Consider arbitrary probabilities $`p_0,\ldots,p_{d-1}`$ and the mixture of
sine vectors of width $`K`$ translated by $`0,\ldots,d-1`$ within an interval
of length $`J=K+d-1`$. Use interval coordinates $`0,\ldots,J-1`$.
Let $`\mathsf L_J`$ be the Dirichlet discrete Laplacian: diagonal entries two,
nearest-neighbor entries minus one, and zero elsewhere. Its eigenvalues are

```math
\lambda_m=2\left(1-\cos\frac{m\pi}{J+1}\right),
\qquad 1\le m\le J.
```

Every translated sine vector has the same expectation

```math
\delta_K^2=2\left(1-\cos\frac\pi{K+1}\right)
```

of $`\mathsf L_J`$. The zeros outside the occupied interval include both
Dirichlet boundary terms; no cyclic shift is used. Therefore the mixture also
has this expectation, for every choice of its weights.

For $`m\ge2`$, the sine chord bound on $`[0,\pi/2]`$ gives

```math
\begin{aligned}
\lambda_m-\lambda_1
&=4\sin\frac{(m+1)\pi}{2(J+1)}
       \sin\frac{(m-1)\pi}{2(J+1)}\\
&\ge\frac{4(m^2-1)}{(J+1)^2}
\ge\frac{12(m-1)}{(J+1)^2}.
\end{aligned}
```

Define the mode-number observable that assigns $`m-1`$ to the eigenvector
of $`\lambda_m`$. Its mean is at most

```math
\mu_{K,d}:=
\frac{(J+1)^2}{12}
\left[\delta_K^2-2\left(1-\cos\frac\pi{J+1}\right)\right].
```

Dephasing in this eigenbasis cannot reduce entropy. The geometric distribution
maximizes Shannon entropy for a given mean mode number, so the same
$`g`$ as in the optical thermal entropy gives

```math
S(\rho)\le g(\mu_{K,d}).
```

This comparison uses an auxiliary Laplacian, rather than identifying its mode
number with the physical photon-number Hamiltonian of the reference.

Put $`r=(d-1)/(K+1)`$. The inequality
$`\sin^2 u-\sin^2 v\le u^2-v^2`$ for $`0\le v\le u\le\pi/2`$
gives a simpler bound:

```math
0\le\mu_{K,d}\le
\overline\mu_{K,d}:=\frac{\pi^2}{12}(2r+r^2).
```

Applying the lemma to every count outcome proves

```math
S(W|Y)=\frac1q\sum_jS(\rho_{W|j})
\le g(\overline\mu_{K,d}).
```

The bound is independent of the helper number distribution. In particular,
$`K=d`$ already gives the constant penalty $`g(\pi^2/4)`$; increasing the
fixed ratio $`K/d`$ makes the displayed penalty arbitrarily small.

## Coherent information includes the discarded reference

Tracing $`W`$ gives the exact phase mixture of the prescribed gate described
in the [finite-reference proof](finite_reference.md#reduced-channel-error-is-quadratic-in-inverse-reference-length).
For the truncated number-diagonal input, the splitter state commutes with
$`N_B+N_Z+N_D`$. Consequently, at each count $`j`$, the ideal receiver states
obtained from different phases are related by receiver number rotations. Their
spectra agree. The actual conditional receiver state is their normalized
mixture, and concavity therefore gives

```math
S(B|Y=j)_{\rm actual}\ge S(B|Y=j)_{\rm ideal}.
```

The reference starts pure, the lift is unitary, and the final count is a
rank-one measurement on the occupied detector subspace. The actual
complementary output is $`ZWY`$, with a copy of the classical record.
Subadditivity and concavity, retaining every outcome, imply

```math
\begin{aligned}
I_c(\tau_{x,d},\Phi_K)
&=\frac1q\sum_j[S(B|j)_{\rm actual}-S(ZW|j)_{\rm actual}]\\
&\ge\frac1q\sum_jS(B|j)_{\rm ideal}-S(Z)
     -g(\overline\mu_{K,d})\\
&\ge-\log_2C_d-S(Z)-g(\overline\mu_{K,d}),
\end{aligned}
```

where $`C_d=\mathrm{Tr}\rho_{B,d}^2+\mathrm{Tr}\rho_{BD,d}^2`$ and the
last line uses the selected ideal detector's purity bound. The actual
complement has been included explicitly; subtracting only the original
inaccessible-output entropy would omit reference information.

Let $`t=[x/(1+x)]^d`$ and $`\kappa(t)=-2\log_2(1-t)`$. The
[finite-cutoff estimate](detector_resources.md#an-explicit-finite-cutoff) now yields

```math
\boxed{
I_c(\tau_{x,d},\Phi_K)
\ge R_1(x)-\kappa(t)-g(\overline\mu_{K,d}).
}
```

The actual channel has finite input, receiver, and record support. The
reference is finite as well. With fresh references it is memoryless, so
ordinary channel coding attains every rate strictly below a positive right
side while retaining the input's strict mean-energy slack.

## A linear stock of prepared reference photons

For a desired reference penalty $`0<\beta\le1`$, let $`y_\beta>0`$ be the
unique solution of $`g(y_\beta)=\beta`$, and define

```math
r_\beta=\sqrt{1+\frac{12y_\beta}{\pi^2}}-1,\qquad
K=\max\left\{1,
\left\lceil\frac{d-1}{r_\beta}\right\rceil-1\right\}.
```

Then $`r\le r_\beta`$ and $`g(\overline\mu_{K,d})\le\beta`$.
The reference's initial mean photon number satisfies

```math
\langle N_W\rangle=h+\frac{K-1}{2}
\le h+\frac{d-1}{2r_\beta}=O_\beta(d).
```

Choose $`x=L=\min\{E,1/b\}`$, with $`1/0=\infty`$, and choose the
cutoff at tolerance $`0<\gamma\le1`$ as in the resource account. The inherited
collective benchmark is credited there to Partial Monitoring. The actual
detector achieves every rate below a positive lower bound of

```math
Q_{\rm coll}(E)-(2+\gamma+\beta).
```

For $`E=L`$ the two in this expression can be replaced by $`\log_2e`$.
At fixed additive tolerances,

```math
\langle N_W\rangle=O_{\gamma,\beta}(L+1),\qquad
\text{record bits per mode}\le\lceil\log_2(q+1)\rceil
=\log_2L+O_{\gamma}(1)\quad(L\ge1).
```

This is a sufficient preparation budget for the specified communication task.
It is compatible with the stronger reference requirement for approximating a
prescribed gate at a separately imposed uniform error. It does not establish a
reference-energy lower bound for capacity, an exact catalyst, sustained reuse,
or an efficient physical synthesis of the conserving control.

## Mean energy exchanged in the actual control

Uniform count probabilities also give the exact mean number after control,
even with the finite reference:

```math
\langle N_D\rangle_{\rm after}=\frac h2,\qquad
\langle N_W\rangle_{\rm after}
=\langle N_W\rangle_{\rm before}+cx_d-\frac h2.
```

The reference supplies $`h/2-cx_d\ge0`$ mean photons to the collected mode.
The inequality uses $`x_d\le(d-1)/2\le h/2`$ and $`0\le c\le1`$.
Multiplying the photon change by $`\hbar\omega`$ gives the corresponding
oscillator energy change. Initial reference stock and net energy transfer are
different quantities. Preparation work, reference reset, and discarded-system
energy are not determined by these equations; the signal budget still prices
incident photons only.

## Verification

The shifted-reference tests check arbitrary mixture weights, the full
Dirichlet spectrum and gap, the entropy estimate, and the explicit choice of
$`K`$. The optical tests separately retain the actual discarded reference in
the complementary channel. Run them with the existing suites:

```bash
python -m unittest discover -s verification -p 'test_*.py' -v
```

Finite tests support the displayed calculations. The written argument gives
the arbitrary-dimensional entropy estimate and the coding consequence.
