# A finite phase reference for the structured detector

[Model](model.md) · [Coherent detector](coherent_measurements.md) · [Record and accuracy resources](detector_resources.md)

The prescribed quadratic-phase Fourier gate can be implemented approximately by
a number-conserving joint unitary using a finite prepared reference. This removes
the ideal infinite phase reference from one explicit detector realization. It
does not supply an efficient laboratory synthesis or a reference reset protocol.

The construction is established machinery. The shift lift is due to
[Åberg, Catalytic Coherence](https://arxiv.org/abs/1304.1060).
[Chiribella, Yang, and Renner](https://arxiv.org/abs/1908.10884), Section IV and
Appendix D, give the finite sine battery, complete energy-sector implementation,
and matching gate-energy scaling. The connection between apparatus coherence and
allowed measurement effects is treated directly by
[Navascués and Popescu](https://arxiv.org/abs/1211.2101). The arguments below make
the constants and the optical-capacity consequence explicit for this detector.

## Apparatus contract

Let $`D`$ be the collected oscillator and $`W`$ a reference ladder with number
operator $`N_W`$. The prepared reference is independent of the signal. The joint
control conserves $`N_D+N_W`$ exactly. After control the helper counts $`D`$ and
discards $`W`$, sending the complete count record to the receiver. All other
number-carrying apparatus resources must be included in this contract; a separate
coherent pointer or nonconserving drive would itself supply a reference.

Arbitrary number-conserving controls within total-number sectors are allowed.
This is a wider operation class than passive linear optics. Gate count, coupling
strength, and execution time are not bounded. The reference state's initial mean
photon number is priced; the thermodynamic work of preparing it is not inferred
from that number.

For the coding construction, every mode receives a fresh independent reference
of the same state. The actual detector is then memoryless. The construction does
not assume that one reference can be reused indefinitely without correlation or
loss of accuracy.

## A finite sine reference and a conserving lift

Let $`q`$ be the odd prime used by the structured detector, $`h=q-1`$, and
$`U=\mathcal F_qD_s`$ on $`|0\rangle,\ldots,|q-1\rangle`$. For any integer
$`K\ge1`$, prepare

```math
|\xi_K\rangle=
\sqrt{\frac2{K+1}}\sum_{\ell=0}^{K-1}
\sin\!\left(\frac{\pi(\ell+1)}{K+1}\right)|h+\ell\rangle_W.
```

Its support and mean photon number are finite:

```math
\mathrm{supp}(\xi_K)\subseteq\{h,\ldots,h+K-1\},
\qquad \langle N_W\rangle=h+\frac{K-1}{2}.
```

One can take a finite reference ladder with levels $`0,\ldots,B_{\max}`$,
where $`B_{\max}=K+2h-1`$. For every complete total-number sector
$`h\le T\le B_{\max}`$, apply $`U`$ to the subspace with basis
$`\{|k,T-k\rangle:0\le k\lt q\}`$. Act as the identity on its orthogonal
complement within that sector and on every other sector. This defines a unitary
$`V_U`$ on detector and reference and exactly conserves total number. For all
occupied initial states,

```math
V_U(|k\rangle|n\rangle)
=\sum_{j=0}^{q-1}U_{jk}|j\rangle|n+k-j\rangle,
\qquad k\lt q,\ h\le n\le h+K-1.
```

The offset $`h`$ keeps every output reference number nonnegative, and the upper
margin keeps it at most $`B_{\max}`$. Initial total number never exceeds that
value. The sector definition supplies unitary completions at both boundaries;
there is no cyclic wraparound. The finite ladder may equivalently be embedded
in an oscillator with identity control outside its relevant sectors.

## Reduced-channel error is quadratic in inverse reference length

Write $`a_n=\langle n|\xi_K\rangle`$ and define the normalized phase density

```math
p_K(\theta)=\frac1{2\pi}\left|\sum_n a_ne^{in\theta}\right|^2,
\qquad -\pi\le\theta\le\pi.
```

The amplitudes are real, so $`p_K`$ is even. Directly tracing the reference
shifts gives the exact channel on the first $`q`$ detector levels:

```math
\mathcal E_{U,K}(\rho)
=\int_{-\pi}^{\pi}p_K(\theta)U_\theta\rho U_\theta^\dagger\,d\theta,
\qquad U_\theta=e^{-iN_D\theta}Ue^{iN_D\theta}.
```

There is no boundary correction for these inputs: all reference shifts in the
contraction lie in the nonnegative spectrum. The offset contributes only a
global phase to the Fourier sum and does not change $`p_K`$.

Centering $`N_D`$ at $`h/2`$ bounds the diamond norm of its commutator generator
$`\mathcal L=-i[N_D,\cdot]`$ by $`h`$. For
$`\mathcal U_\theta=\mathrm{Ad}_{U_\theta}`$,

```math
\mathcal U_\theta''
=\mathcal L^2\mathcal U_\theta
 -2\mathcal L\mathcal U_\theta\mathcal L
 +\mathcal U_\theta\mathcal L^2,
\qquad \|\mathcal U_\theta''\|_\diamond\le4h^2.
```

Taylor expansion therefore has remainder at most $`2h^2\theta^2`$ in diamond
norm. Evenness cancels the first-order term after integration. Thus

```math
\frac12\|\mathcal E_{U,K}-\mathcal U\|_\diamond
\le h^2\mathbb E_{p_K}[\theta^2].
```

The sine amplitudes have one-step overlap
$`\sum_na_na_{n+1}=\cos[\pi/(K+1)]`$. Consequently

```math
\delta_K^2:=\mathbb E_{p_K}[4\sin^2(\theta/2)]
=2\left(1-\cos\frac\pi{K+1}\right)
\le\frac{\pi^2}{(K+1)^2}.
```

On $`[-\pi,\pi]`$, $`\theta^2\le\pi^2\sin^2(\theta/2)`$. Combining the
bounds gives the explicit sufficient estimate

```math
\frac12\|\mathcal E_{U,K}-\mathcal U\|_\diamond
\le\min\!\left\{1,\frac{\pi^2h^2\delta_K^2}{4}\right\}
\le\min\!\left\{1,\frac{\pi^4h^2}{4(K+1)^2}\right\}.
```

For a target $`0<\varepsilon\le1`$, it suffices to choose

```math
K=\max\!\left\{1,
\left\lceil\frac{\pi^2(q-1)}{2\sqrt\varepsilon}\right\rceil-1\right\}.
```

The prepared reference then has mean photons $`O(q/\sqrt\varepsilon)`$.
Counting and tracing further systems cannot increase this error. The same bound
therefore holds for the full receiver-plus-record channel, including a
purifying signal reference. Unlike the ideal rank-one detector, its true
complement can contain residual information in $`W`$; the operational error
bound and $`-S(R|BY)`$ treatment keep that information in the rate account.

The reduced-channel estimate does not imply product return at error
$`\varepsilon`$. A separate controlled-shift comparison gives joint-vector
error at most $`h\delta_K=O(h/K)`$ for odd $`q`$: use shifts centered at
$`h/2`$ and telescope one-step reference differences. This establishes only a
single-use approximate product return at the larger error scale. Exact return,
reset work, and sustained reuse at fixed $`K`$ are not established.

## Matching energy order for the prescribed gate

The following lower bound is an application of the gate-implementation theorem
of Chiribella, Yang, and Renner, Appendix A, Corollary 3, Eq. (A10), with the
half-diamond conversion in Appendix D. It concerns approximating the entire
unitary channel on all $`q`$ levels, with the battery discarded and with no
battery-return premise.

Let $`\Delta=U^\dagger N_DU-N_D`$ and
$`r_U=\lambda_{\max}(\Delta)-\lambda_{\min}(\Delta)`$. Any implementation in
that conserving battery model with half-diamond error at most $`\varepsilon`$
has initial battery mean photons obeying

```math
\langle N_W\rangle\ge
\frac{r_U^2}{32h\sqrt{2\varepsilon}}-2h\sqrt{2\varepsilon}.
```

Here the energy unit is one photon and the system Hamiltonian is
$`N_D=\mathrm{diag}(0,\ldots,h)`$. For $`U=\mathcal F_qD_s`$, every diagonal
entry of $`U^\dagger N_DU`$ equals $`h/2`$. Rayleigh quotients on the two
extreme number states therefore give $`r_U\ge h`$. In particular,

```math
\langle N_W\rangle\ge
\frac{q-1}{64\sqrt{2\varepsilon}},
\qquad 0<\varepsilon\le1/256.
```

The lower statement treats the target as a finite system of $`q`$ levels.
Additional number-bearing apparatus degrees of freedom must be included in the
battery rather than supplied without a charge.

Together with the construction, the initial reference energy for uniformly
implementing this prescribed gate has order $`q/\sqrt\varepsilon`$ at small
error. This matching gate-level bound is inherited from the cited theorem. It
does not lower-bound arbitrary measurements that reproduce the same classical
record, implementations tested only on one average input, or all detectors that
attain a given communication rate.

The [first-moment capacity converse](reference_mean_bounds.md) addresses that
different optimization under separate local conservation. It proves linear
mean-stock necessity for a bounded rate gap in the energy-driven regime,
independently of this prescribed-gate theorem.

## Optical rate with a finite prepared reference

Choose the cutoff $`d`$ at energy $`L=\min\{E,1/b\}`$ and tolerance
$`\gamma`$ as in the [resource account](detector_resources.md). Let

```math
\varepsilon_\beta=\frac{\beta}{4\log_2(8d/\beta)},
\qquad 0<\beta\le1.
```

Select the ideal quadratic setting there, then use the conserving lift with a
fresh sine reference whose $`K`$ satisfies the bound above at error
$`\varepsilon_\beta`$. The actual memoryless detector achieves every rate
strictly below a positive lower bound of

```math
Q_{\rm coll}(E)-(2+\gamma+\beta).
```

Its classical outcome alphabet still has at most $`q+1`$ symbols. At fixed
cutoff and rate tolerances, the sufficient prepared reference mean is

```math
\langle N_W\rangle
=O\!\left((L+1)\sqrt{\ln(L+2)}\right),
```

while the record cost is $`\log_2L+O(1)`$ bits per mode for $`L\ge1`$.
The reference mean counts supplied stock at the start of each use, not net
consumed energy or dissipated work. The stronger gate-level lower bound does
not establish that this stock scaling is necessary for the capacity task.

For the communication task, the [direct reference-entropy argument](direct_reference.md)
gives the sharper sufficient mean stock $`O_{\gamma,\beta}(L+1)`$ at the same
fixed additive rate tolerances. It bounds information in the actual discarded
reference rather than imposing a shrinking uniform gate error. The
$`O((L+1)\sqrt{\ln(L+2)})`$ estimate above remains a sufficient consequence
of the uniform gate-accuracy route.

For the number-diagonal helper average input, the finite-reference implementation
still gives a uniform distribution over the $`q`$ final detector numbers. Exact
total-number conservation therefore fixes the mean reference change:

```math
\langle N_W\rangle_{\rm final}
=\langle N_W\rangle_{\rm initial}+cx_d-\frac{q-1}{2}.
```

This is energy transferred to the measured oscillator, rather than a statement
about irreversible work or the possibility of recovering that energy later.

## An invariant apparatus cannot supply the missing coherence

Suppose instead that the initial apparatus state $`\sigma_W`$ commutes with
$`N_W`$, the joint control commutes with $`N_D+N_W`$, and every readout effect
is invariant under the same total-number rotations. Covariance implies that
each induced helper effect commutes with $`N_D`$. Its Fock-basis matrix is
therefore diagonal. By the [counting simulation](counting_bounds.md#every-number-diagonal-record-is-simulated-by-counting),
this apparatus cannot beat counting, even with arbitrary receiver coding.

This is the standard energy-conservation measurement obstruction of the cited
apparatus literature, applied to the current detector classes. It fails to apply
if another coherent control or pointer already supplies an external reference.
Nonzero apparatus coherence is necessary under the stated symmetry contract;
this statement alone is not a quantitative capacity-versus-reference-energy
lower bound.

The restriction is per collected mode. For joint processing of several modes,
total photon number has degenerate eigenspaces; invariance can retain coherence
between different occupation vectors of the same total number. This single-mode
argument does not impose counting's ceiling on all such collective measurements.

## Verification

The finite-reference tests explicitly construct the conserving sector unitary,
trace its reference, and compare the resulting channel with the exact phase
mixture. They check entangled inputs, lower-boundary handling, total-number
conservation, sine-state moments, and the optical receiver's actual reference
state. The written arguments and cited gate theorem establish the uniform
diamond bound and asymptotic resource statements.
