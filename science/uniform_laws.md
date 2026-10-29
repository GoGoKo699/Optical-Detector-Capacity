# Uniform energy–collection crossover and finite separation

[Model](model.md) · [Counting bounds](counting_bounds.md) · [Coherent construction](coherent_measurements.md)

## Uniform domain

Fix $`0\lt a\lt 1`$, set $`b_0=\frac12\min\{a,1-a\}`$, and allow $`E\ge1`$, $`0\le b\le b_0`$. Then $`a>b`$ and $`c\ge c_0=(1-a)/2>0`$. Define

```math
L=\min\{E,1/b\},\qquad 1/0=\infty.
```

There are finite constants depending on $`a`$ only such that throughout this domain

```math
Q_{\rm cnt}(E)=\frac12\log_2L+O_a(1),
\qquad
Q_1(E)=Q_{\rm coll}(E)+O(1)=\log_2L+O_a(1).
```

In particular, the remainders stay bounded along arbitrary joint paths with $`E\to\infty`$, $`b\to0`$, and $`L\to\infty`$. The received fraction is held fixed; the statement is not uniform as $`a`$ approaches zero or one.

## Counting upper and lower orders

The [energy converse](counting_bounds.md) gives $`U_E\le\frac12\log_2E+C_E(a)`$ because $`c\ge c_0`$. For $`b>0`$, the loss converse gives $`U_b\le\frac12\log_2(1/b)+C_b(a)`$: $`1-b\ge1/2`$ and the remaining factors are bounded in this domain. Taking the smaller of these inequalities yields the upper half-logarithm. At $`b=0`$, the energy bound alone applies.

For the lower bound, choose the thermal mean $`X=L`$. It is allowed because $`L\le E`$, and $`bL\le1`$. The quantities in the thermal construction obey

```math
\mu=\frac{aL}{1+cL}\ge\frac a2,\quad
\mu(1+\mu)\ge w_0:=\frac a2\left(1+\frac a2\right),\quad
g(bL)\le g(1)=2.
```

Since $`1+cL\ge c_0L`$, its finite bound gives explicitly

```math
Q_{\rm cnt}(E)\ge\frac12\log_2L
+\frac12\log_2(c_0w_0)+\log_2(4/\pi)
-\frac12\log_2e-2.
```

A negative right side is simply weaker than zero capacity. The lower and upper bounds prove the uniform claim without optimizing the additive constant or assuming finite photon-number variance.

## Full leading rate for individual-mode processing

The elementary inequalities

```math
\log_2(1+x)\le g(x)\le\log_2(1+x)+\log_2e
```

show that $`g(aE)-g(bE)`$ differs from $`\log_2[(1+aE)/(1+bE)]`$ by a bounded constant. Splitting into $`bE\le1`$ and $`bE\ge1`$ gives

```math
\frac a2L\le\frac{1+aE}{1+bE}\le(1+a)L.
```

Thus the collective capacity is $`\log_2L+O_a(1)`$. The [constant-gap bound](coherent_measurements.md) from restricting the helper to individual modes supplies the same leading law for $`Q_1`$.

The counting disadvantage is therefore $`\frac12\log_2L+O_a(1)`$, and the ratio $`Q_1/Q_{\rm cnt}`$ tends to two as $`L\to\infty`$. For fixed positive inaccessible loss, increasing energy eventually saturates these asymptotic scales; a factor-of-two limit is not claimed by varying energy alone at that fixed loss.

## Finite-energy example with a rational certificate

Use $`a=1/4`$, $`b=1/10000`$, $`c=7499/10000`$, and $`E=10^6`$. The formulas give

```math
R_1(E)\simeq10.5158732900,\qquad
U_b\simeq7.8983983862,\qquad
Q_{\rm coll}(E)\simeq11.2805257151.
```

The [verification program](../verification/verify.py) also proves the wider rational enclosures

```math
10.51\lt R_1(E)\lt 10.52,\qquad
Q_{\rm cnt}(E)\lt 7.90,\qquad
11.28\lt Q_{\rm coll}(E)\lt 11.29.
```

It evaluates logarithms using range reduction and the rational series

```math
\ln x=2\sum_{k=0}^{m-1}\frac{t^{2k+1}}{2k+1}+R_m,
\quad t=\frac{x-1}{x+1},\quad
0\le R_m\le\frac{2t^{2m+1}}{(2m+1)(1-t^2)}
```

on $`1\le x\le2`$. Forty-eight terms suffice. The counting certificate uses $`\pi<22/7`$, giving a slightly relaxed upper bound below 7.90. All certification comparisons use exact fractions, not floating-point optimizer output. The resulting strict gap exceeds 2.61 qubits per mode. This is a high-energy illustration of rigorous capacity bounds, not an experimental efficiency claim.

## Boundary cases

At $`E=0`$ all capacities vanish. At $`a\le b`$, joint antidegradability makes them zero even with collective measurements. At $`b=0`$, the effective scale is $`L=E`$ and $`Q_{\rm coll}=g(aE)`$.

At $`c=0`$, there is no collected output: all three classes reduce to ordinary pure-loss communication, with capacity $`\max\{g(aE)-g(bE),0\}`$. The half-logarithmic law does not apply to that boundary. At $`a=1`$, the identity channel has capacity $`g(E)`$ for every class; this is excluded by the fixed-$`0\lt a\lt 1`$ crossover domain.

Neither a finite-energy exact counting maximizer nor an exact value for $`Q_1`$ is asserted. Those are different optimization questions from the established detector-class laws.
