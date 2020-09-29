---
title: "MGPCG"
categories: "Simulation"
tags: physics, simulation
date: 2020-09-29
---

# Conjugate Gradient

## Gradient Descent

::: incremental
* **Problem**: $\mathbf{A}\mathbf{x}=\mathbf{b}$, $\mathbf{A}$ is SPD(symmetric positive-definite)
* The solution $\mathbf{x}^*$ minimize this function:$f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^TA\mathbf{x}-\mathbf{x}^T\mathbf{b}$ 
* **Property**: The gradient at $\mathbf{x}$ is $\nabla f = \mathbf{A}\mathbf{x}-\mathbf{b}=-\mathbf{r}$ 
* Interative solver: $\mathbf{x}_{k+1} = \mathbf{x}_k + \alpha_k \mathbf{r}_k$, find $\alpha_k$ to minimize $f(\mathbf{x}_{k+1})$

:::

## Gradient Descent Algorithm

```python
while r.norm() > err:
    r = b - A*x
    a = r.dot(r)/(r.transpose()*A*r)
    x = x + a*r
```
::: incremental
* **Pros**: Applied to any kind of equation
* **Cons**: Slow

:::

## Conjugation

* $\mathbf{A}$ is SPD
* **Definition**: $\mathbf{u}$ and $\mathbf{v}$ are **conjugate** if 
$$
\langle \mathbf{u},\mathbf{v}\rangle_A := \mathbf{u}^T\mathbf{A}\mathbf{v} =0
$$

## Conjugate Vectors Basis

::: incremental
* **Property**: $P=\{\mathbf{p}_1,\cdots,\mathbf{p}_n\}$ and $\langle \mathbf{p}_i, \mathbf{p}_j \rangle_A = \delta_{ij}$, then $P$ forms a basis of $\mathbb{R}^n$
* Suppose the solution of $\mathbf{A}\mathbf{x}=\mathbf{b}$ is $\mathbf{x}^*$, we can decompose it as 
$$
\mathbf{x}^* = \sum_{i=1}^n\alpha_i\mathbf{p}_i$$
* Then we can easily get 
$$
\alpha_k = \frac{\langle \mathbf{p}_k, \mathbf{b}\rangle}{\langle \mathbf{p}_k, \mathbf{p}_k\rangle_A}$$ 
:::

## As Interative Solver

::: incremental
* Find a sequence of $n$ conjugate directions and corresponding $\alpha_k$
* Stop for at most $n$ steps
:::


