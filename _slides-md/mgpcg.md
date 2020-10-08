---
title: "MGPCG"
categories: "Simulation"
tags: physics, simulation
author: Liangwang Ruan
date: 2020-10-2
---

# G: Gradient

## Gradient Descent

::: incremental
* **Problem**: $\mathbf{A}\mathbf{x}=\mathbf{b}$, $\mathbf{A}$ is SPD(symmetric positive-definite)
* The solution $\mathbf{x}^*$ minimize this function:$f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^TA\mathbf{x}-\mathbf{x}^T\mathbf{b}$ 
* **Property**: The gradient at $\mathbf{x}$ is $\nabla f = \mathbf{A}\mathbf{x}-\mathbf{b}=-\mathbf{r}$ 
* Iterative solver: $\mathbf{x}_{k+1} = \mathbf{x}_k + \alpha_k \mathbf{r}_k$, find $\alpha_k$ to minimize $f(\mathbf{x}_{k+1})$

:::

## Gradient Descent Algorithm

```python
while r.norm() > err:
    r = b - A*x
    a = r.dot(r)/(r.transpose()*A*r)
    x = x + a*r
```
::: incremental
* **drawback**: Slow convergence

:::

# CG: +Conjugacy

## conjugacy

* $\mathbf{A}$ is SPD
* **Definition**: $\mathbf{u}$ and $\mathbf{v}$ are **conjugate** if 
$$
\langle \mathbf{u},\mathbf{v}\rangle_A := \mathbf{u}^T\mathbf{A}\mathbf{v} =0
$$

## Conjugate Vectors Basis

::: incremental
* **Property**: $P=\{\mathbf{p}_0,\cdots,\mathbf{p}_{n-1}\}$ and $\langle \mathbf{p}_i, \mathbf{p}_j \rangle_A = \delta_{ij}$, then $P$ forms a basis of $\mathbb{R}^n$
* Suppose the solution of $\mathbf{A}\mathbf{x}=\mathbf{b}$ is $\mathbf{x}^*$, we can decompose it as 
$$
\mathbf{x}^* = \sum_{i=0}^{n-1}\alpha_i\mathbf{p}_i$$
* Using conjugacy property we have:$\alpha_k = \frac{\langle \mathbf{p}_k, \mathbf{b}\rangle}{\langle \mathbf{p}_k, \mathbf{p}_k\rangle_A}$
:::

## As Interative Solver

:::: {.columns}
::: {.column width="70%"}

::: incremental
* Find a sequence of $n$ conjugate directions and corresponding $\alpha_k$
* Stop for at most $n$ steps or even faster if $P$ is well choosed, faster than steepest descent
* No need to calculate the inverse of the Hessian matrix like in Newton method
* How to find $P$?
:::

:::
::: {.column width="30%"}

![](/assets/images/conjugate-gradient.png){height="400px"}

:::
::::

## Key Observation

::: incremental
* Suppose $P$ is known, and $\mathbf{r}_0 = \mathbf{p}_0$
* Follow iteration steps, let $\alpha_k$ minimize $f(\mathbf{x}_k+\alpha_k\mathbf{p}_k)$, then we have $\alpha_k = \frac{\mathbf{r}_k^T\mathbf{p}_k}{\langle \mathbf{p}_k, \mathbf{p}_k \rangle_A}$
* **Define**: $B_k = span\{\mathbf{p}_0,\cdots,\mathbf{p}_{k-1}\}$
* **Theorem**: $\mathbf{x}_k$ minimize $f(\mathbf{x})$ in subspace $\mathbf{x}_0+B_k$, since $B_n = \mathbb{R}^n$, $\mathbf{x}_n = \mathbf{x}^*$
* **Lemma**: $\mathbf{r}_k \perp B_k$
:::

::: notes
* $\mathbf{r}_k$ is gradient, so lemma leads to theorem
* step k is the best result in $B_k$, stronger insurance than pure gradient descentb
* proof using SPD property and P is conjugate basis
:::

## Inductive Proof

::: incremental
* Initially $\mathbf{r}_0 \perp B_0=\phi$
* $\mathbf{r}_{k+1} \perp \mathbf{p}_k$ since $\alpha_k$ minimize $f(\mathbf{x}_k+\alpha_k\mathbf{p}_k)$ and $\mathbf{r}_{k+1}=-\nabla f(\mathbf{x}_{k+1})$
* $\mathbf{r}_{k+1} = \mathbf{b} - \mathbf{A}\mathbf{x}_{k+1}=\mathbf{r}_k-\alpha_k\mathbf{A}\mathbf{p}_k$
* $\mathbf{r}_k \perp B_k$ (induction) and $\alpha_k\mathbf{A}\mathbf{p}_k \perp B_k$ (conjugacy) $\implies \mathbf{r}_{k+1} \perp B_k$
* $\implies \mathbf{r}_{k+1} \perp B_{k+1}$
:::

## Key Observation

::: incremental
* Let $P$ be $\{\mathbf{r}_k\}$'s Gram-Schimidt orthogonalization: $\mathbf{p}_i = \mathbf{r}_i + \sum_{k=0}^{i-1}\beta_{ik}\mathbf{p}_k$
* Rewrite $\mathbf{r}_i = \mathbf{p}_i - \sum_{k=0}^{i-1}\beta_{ik}\mathbf{p}_k$, also $\mathbf{r_k} \perp B_k$ $\implies \mathbf{r}_i^T\mathbf{r}_j=0$ for $i \neq j$, $\{\mathbf{r}_k\}$ is othogonal basis
* $\beta_{ik} = - \frac{\mathbf{r}_i^T\mathbf{A}\mathbf{p}_k}{\langle \mathbf{p}_k,\mathbf{p}_k\rangle_A}$ also $\mathbf{r}_{k+1}=\mathbf{r}_k-\alpha_k\mathbf{A}\mathbf{p}_k$ $\implies \beta_{ik}=\frac{\mathbf{r}_i^T\mathbf{r}_{k+1}-\mathbf{r}_i^T\mathbf{r}_{k}}{\mathbf{r}_k^T\mathbf{r}_k}$ non-zero when $k=i-1$
* Then can be simplified to $\mathbf{p}_k = \mathbf{r}_k-\beta_{k-1}\mathbf{P}_{k-1}$, where $\beta_{k-1} = \frac{\mathbf{r}_k^T\mathbf{r}_k}{\mathbf{r}_{k-1}^T\mathbf{r}_{k-1}}$
:::

## Conjugate Gradient Algorithm 

```python
r = b - A*x
p = r
p_pre = p
r_pre = r
k = 0
while r.norm() > err and k < n:
    alpha = r.dot(r)/(p.transpose()*A*p)
    x = x + alpha*p_pre
    r = r_pre - alpha*A*p_pre
    beta = r.dot(r)/r_pre.dot(r_pre)
    p = r + beta*p_pre
    p_pre = p
    r_pre = r
    k += 1
```

## Convergence

* **Theorem**: $\mathbf{e}_i = \mathbf{x}_i-\mathbf{x}^*$, $\kappa(\mathbf{A})$ is condition number $\lVert \mathbf{A}^{-1} \rVert\cdot \lVert \mathbf{A} \rVert$, then 
$$\lVert\mathbf{e}_k\rVert_\mathbf{A} \leq 2\left( \frac{\sqrt{\kappa(\mathbf{A})}-1}{\sqrt{\kappa(\mathbf{A})}+1} \right)^k \lVert \mathbf{e}_0 \rVert_\mathbf{A}$$
* Smaller $\kappa(\mathbf{A})$, Faster Convergence!

# PCG: +Precondition

## Preconditioning

::: incremental
* $\mathbf{M}$ is a SPD matrix that approximates $\mathbf{A}$ but easy to invert
* $\mathbf{M}^{-1}\mathbf{A}$ is better conditioned than $\mathbf{A}$
* Suppose $\mathbf{M} = \mathbf{E}\mathbf{E}^T$, we can solve 
$$\mathbf{E}^{-1}\mathbf{A}\mathbf{E}^{-T}\hat{\mathbf{x}} = \mathbf{E}^{-1}b,\ \hat{\mathbf{x}} = \mathbf{E}^T\mathbf{x}$$
:::

## Variable Substitutions

::: incremental
* Directly apply preconditioning to CG we can get something like $\alpha_k = \frac{\hat{\mathbf{r}}_k^T\hat{\mathbf{r}}_k}{\hat{\mathbf{p}}_k^T\mathbf{E}^{-1}\mathbf{A}\mathbf{E}^{-T}\hat{\mathbf{p}}_k}$
* To simplify, let $\mathbf{r}_i = \mathbf{E}\hat{\mathbf{r}}_i$, $\mathbf{p}_i = \mathbf{E}^{-T}\hat{\mathbf{p}}_i$, $\mathbf{x} = \mathbf{E}^{-T}\hat{\mathbf{x}}$, $\mathbf{E}^{-T}\mathbf{E}^{-1}=\mathbf{M}^{-1}$
* $\mathbf{E}$ disappears, only $\mathbf{M}^{-1}$ left, $\alpha_k = \frac{\mathbf{r}_k^T\mathbf{M}^{-1}\mathbf{r}_k}{\mathbf{p}_k^T\mathbf{A}\mathbf{p}_k}$
:::

## PCG Algorithm

```python
r = b - A*x
p = M.inverse()*r
p_pre = p
r_pre = r
k = 0
while r.norm() > err and k < n:
    alpha = r.transpose()*M.inverse()*r/(p.transpose()*A*p)
    x = x + alpha*p_pre
    r = r_pre - alpha*A*p_pre
    beta = r.transpose()*M.inverse()*r/r_pre.transpose()*M.inverse()*r_pre
    p = M.inverse()*r + beta*p_pre
    p_pre = p
    r_pre = r
    k += 1
```

## Different M

::: incremental
* **Jacobi**: $\mathbf{M} = diag\{a_{11}, a_{22}, \cdots, a_{nn}\}$
* **Block Jacobi**: blocked diagnal
* **Incomplete Cholesky**: imcomplete Cholesky Factorization($\mathbf{A}=\mathbf{R}^T\mathbf{R}$ where $\mathbf{R}$ is upper triangle matrix), $\mathbf{M}=\hat{\mathbf{R}}^T\hat{\mathbf{R}}$, not for all $\mathbf{A}$
* If $\mathbf{A}$ is irreducibly diagonally dominant, **ICPCG** works, that is
  * $\lvert a_{jj} \rvert \geq \sum_{i\neq j} \lvert a_{ij} \rvert$, $j=1,\cdots,n$
  * no permutation such that $\mathbf{P}\mathbf{A}\mathbf{P}^T=diag\{\mathbf{A}_1,\mathbf{A}_2\}$ 
:::

# MG: MultiGrid

## Jacobi Iteration (Relaxation)

::: incremental
* **Define**: $\mathbf{A} = \mathbf{D} + \mathbf{L} + \mathbf{U}$
* At every step: $\mathbf{x}_{n+1} = -\mathbf{D}^{-1}(\mathbf{L}+\mathbf{U})\mathbf{x}_n+\mathbf{D}^{-1}\mathbf{b}$
* Iteration matrix: $\mathbf{T} = -\mathbf{D}^{-1}(\mathbf{L}+\mathbf{U})$
* **Define**(spectral radius): $\rho(\mathbf{T})=\max \{|\lambda_1|, \cdots, |\lambda_n|\}$
* **Theorem**: $\lVert \mathbf{e}_k \rVert \leq \rho(\mathbf{T})^k\lVert \mathbf{e}_0 \rVert$, usually we have $\rho(\mathbf{T}) = 1-O(\frac{1}{n^2})$, slow convergence when large $n$

:::

## A Simple Case

::: incremental
* **Problem**: $\frac{d^2 u}{dx^2}=0$, $u(0)=0$, $u(1)=0$
* Analytical solution: $u=0$
* Discretize $[0,1]$ into $N$ elements $\implies \mathbf{A}\mathbf{u}=\mathbf{0}$, where
$$\mathbf{A}=\begin{pmatrix}
    2 & -1 & &  \\
    -1 & 2 & -1 &  \\
    &  & \ddots & \\
    & & -1 & 2
\end{pmatrix}$$

:::

## Try Jacobi

:::: {.columns}
::: {.column width="60%"}

::: incremental
* $\mathbf{T}=-\mathbf{D}^{-1}(\mathbf{L}+\mathbf{U})=\mathbf{I}-\frac{1}{2}\mathbf{A}$
* $\mathbf{A}\mathbf{w}=\lambda\mathbf{w} \implies$ $\mathbf{w}^k=\{0, \frac{k\pi}{N},\cdots, \frac{(N-1)k\pi}{N}\}$, $\lambda^k = 4\sin^2(\frac{k\pi}{2N})$
* $1-\frac{1}{2}\lambda^k=1-2\sin^2(\frac{k\pi}{2N})$
* **low** frequency components converge **slower**
:::

:::

::: {.column width="40%"}

![](/assets/images/w-lambda.png){height="400px"}

:::
::::

## Key Observation

::: incremental
* Coarse grid can be used to compute an improved initial guess for the fine grid
* Relaxation on coarse grid is much faster
* Iteration:
  * relax on $\mathbf{A}\mathbf{x}=\mathbf{b}$ on coarser grid ($\Omega^{2h}$)
  * **Prolongation**: interpolation solution onto finer grid ($\Omega^h$) as initial guess
  * relax on $\Omega^h$
* What if the error still has smooth components when we get to the fine grid?

:::

## Key Observation

::: incremental
* After relaxation on $\Omega^h$ the error is smooth, more oscillatory on coarser grid
* For any vector $\mathbf{x}$, error $\mathbf{e}=\mathbf{x}^*-\mathbf{x}$ satisfies $\mathbf{A}\mathbf{e}=\mathbf{r}$, where $\mathbf{r}=\mathbf{b}-\mathbf{A}\mathbf{x}$ 
* Error Correction
  * **Restriction**: restrict the residual from $\Omega^h$ to $\Omega^{2h}$
  * Relaxation $\mathbf{A}\mathbf{e}=\mathbf{r}$ on $\Omega^{2h}$ to get $\mathbf{e}^{2h}$
  * Interpolation back to $\Omega^{h}$ and add it to $\mathbf{x}^h$

:::

## Two-grid scheme

::: incremental
* Relax $\mathbf{A}^h\mathbf{x}^h=\mathbf{b}^h$ on $\Omega^h$ to get $\mathbf{x}^h$ 
* Compute residual: $\mathbf{r}^h = \mathbf{b}^h-\mathbf{A}^h\mathbf{x}^h$
* Restrict the residual to $\Omega^{2h}$: $\mathbf{r}^{2h}=\mathbf{I}_{h}^{2h}\mathbf{r}^h$
* Solve $\mathbf{A}^{2h}\mathbf{e}^{2h}=\mathbf{r}^{2h}$ on $\Omega^{2h}$
* Prolong the error to $\Omega^h$: $\mathbf{e}^h=\mathbf{I}_{2h}^h\mathbf{e}^{2h}$
* Correct solution: $\mathbf{x}^h \gets \mathbf{x}^h+\mathbf{e}^h$
* Relax on $\Omega^h$ again using $\mathbf{x}^h$ as initial guess
:::

## V-Cycle Algorithm

![](/assets/images/multigrid.png){height="400px"}

## Different Types

![](/assets/images/MultigridWork.svg){width="100%"}

## MG as Preconditioner

::: incremental
* Begin with zero initial guess at $\Omega^h$ $\implies$ procedure is linear operation
* To insure SPD, sufficient conditions are:
  * restriction/prolongation operations are transpose of one another
  * smoother used in upstroke and downstroke should be in reverse order
  * the solve at coarsest level should be exact or SPD insured iteration method

:::

# MGPCG for Fluid

## Background

* **Problem**: $\nabla^2p=f$ in $\Omega$, $p(\mathbf{x})=\alpha(\mathbf{x})$ on $\Gamma_D$, $p_n(\mathbf{x})=\beta(\mathbf{x})$ on $\Gamma_N$

. . .

* **Discretization**: $\frac{1}{h^2}\sum_{(i',j',k')\in N^*_{ijk}}p_{i'j'k'}-p_{ijk}=f_{ijk}$, where $N^*_{ijk}=\{(i',j',k') \in N_{ijk}: cell (i',j',k') \notin \Gamma_N\}$

![](/assets/images/mgpcg-discretization.png){width="100%"}

## Prolongation/Restriction

:::: {.columns}
::: {.column width="60%"}
* $R=B\otimes B\otimes B$
* $P^T=8B\otimes B\otimes B$
:::

::: {.column width="40%"}
![](/assets/images/mgpcg-restriction.png)
:::
::::

## Smooth

* No explicit matrix stored

```python
# the same as Stable Fluids!
@ti.kernel
def smooth(l: ti.template(), phase: ti.template()):
# phase = red/black Gauss-Seidel phase
  for i, j, k in r[l]:
    if (i + j + k) & 1 == phase:
      z[l][i,j,k] = (r[l][i,j,k]+z[l][i+1,j,k]+z[l][i-1,j,k] \
        +z[l][i,j+1,k]+z[l][i,j-1,k] \
        +z[l][i,j,k+1]+z[l][i,j,k-1])/6.0
```

## Boundary

* Only prolongate/restrict into interior cells
* Extra smoothing on boundary band cells

# Reference

* Jonathan Richard Shewchuk, [An Introduction to the Conjugate Gradient Method Without the Agonizing Pain](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf)
* William L. Briggs, [A Multigrid Tutorial](https://www.math.ust.hk/~mawang/teaching/math532/mgtut.pdf)
* A. McAdams, E. Sifakis, and J. Teran. 2010. [A parallel multigrid Poisson solver for fluids simulation on large grids](http://pages.cs.wisc.edu/~sifakis/papers/mgpcg_poisson.pdf). In Proceedings of the 2010 ACM SIGGRAPH/Eurographics Symposium on Computer Animation (SCA '10). Eurographics Association, Goslar, DEU, 65–74.
