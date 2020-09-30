---
title: "MGPCG"
categories: "Simulation"
tags: physics, simulation
date: 2020-09-29
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
* $\beta_{ik} = - \frac{\mathbf{r}_i^T\mathbf{A}\mathbf{p}_k}{\langle \mathbf{p}_k,\mathbf{p}_k\rangle_A}$ also $\mathbf{r}_{k+1}=\mathbf{r}_k-\alpha_k\mathbf{A}\mathbf{p}_k$ $\implies \beta_{ik}=\frac{\mathbf{r}_i^T\mathbf{r}_{k+1}-\mathbf{r}_i^T\mathbf{r}_{k}}{\mathbf{r}_i^T\mathbf{r}_i}$ non-zero when $k=i-1$
* Then can be simplified to $\mathbf{p}_k = \mathbf{r}_k-\beta_{k-1}\mathbf{P}_{k-1}$, where
$$\beta_{k-1} = \frac{\mathbf{r}_k^T\mathbf{r}_k}{\mathbf{r}_{k-1}^T\mathbf{r}_{k-1}}$$
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