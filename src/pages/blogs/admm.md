---
title: ADMM
---

# ADMM

<div class="p-2 rounded-lg bg-green-50 dark:bg-gray-800">
PD,ADMM,Friction
</div>

## 增广拉格朗日函数法（ALM）

对于一般形式的优化问题：

\begin{equation}
  \begin{aligned}
    \min f(\b{x}) \\
    \b{c}(\b{x}) = \b{0}
  \end{aligned}
\end{equation}

我们定义其增广拉格朗日函数 （Augmented Lagrangian Function）为（下面这个形式为推导方便与一般教科书中不同）：

\begin{equation}
  \begin{aligned}
    L(\b{x},\b{\lambda}) &:= f(\b{x}) + \b{\lambda}^T \bb{W} \b{c} + \frac{1}{2}\b{c}^T\bb{W}\b{c} \\
    & = f(\b{x}) + \frac{1}{2}\lVert \b{c} + \b{\lambda} \rVert_{\bb{W}}^2 - \frac{1}{2} \lvert \b{\lambda} \rVert_{\bb{W}}^2
  \end{aligned}
\end{equation}

可以看为是在一般拉格朗日函数的基础上加上二次罚函数项。一般的二次罚函数方法需要不断加大权重$\bb{W}$来使得约束最终满足，而加上拉格朗日项之后可以保证在收敛到后面时拉格朗日项会发挥主要作用得到正确的约束力，于是迭代全程就可以使用相同的罚函数权重$\bb{W}$，并且收敛还能更快。

我们通过交替迭代$\b{x}$和$\b{\lambda}$逐渐收敛到原问题的解。在每一步迭代中，固定拉格朗日乘子$\b{\lambda}^l$时，增广拉格朗日函数类似于二次罚函数的形式，可以求解无约束最小化问题更新$\b{x}$的值：
$$\b{x}^{l+1} \gets \min L(\b{x},\b{\lambda}^l)$$
接下来如何更新$\b{\lambda}^{l+1}$？我们希望拉格朗日乘子最终能正确反应约束力，也就是能够满足原问题的KKT条件：
$$\nabla f(\b{x}^*) + \b{\lambda}^{*T}\bb{W}\nabla \b{c}(\b{x}^*) = 0$$
而在迭代中有每一步的$\b{x}^{l+1}$满足：
$$\nabla f(\b{x}^{l+1}) + (\b{c}(\b{x}^{l+1}) + \b{\lambda}^l)^T\bb{W}\nabla \b{c}(\b{x}^{l+1}) = 0$$
我们希望这两个条件在迭代后期能相容，也就表明在$l$比较大之后应该有$\b{c}(\b{x}^{l+1}) + \b{\lambda}^l \approx \b{\lambda}^{*}$，那么一个自然的更新$\b{\lambda}$的想法就是$\b{\lambda}^{l+1} \gets \b{c}(\b{x}^{l+1}) + \b{\lambda}^l$。总结一下，增广拉格朗日函数法在每一步中的迭代操作如下：

\begin{equation}
  \begin{aligned}
    \b{x}^{l+1} &\gets \min L(\b{x},\b{\lambda}^l) \\
    \b{\lambda}^{l+1} &\gets \b{c}(\b{x}^{l+1}) + \b{\lambda}^l
  \end{aligned}
\end{equation}

## 交替方向乘子法（ADMM）

ADMM求解的一般问题如下：

\begin{equation}
  \begin{aligned}
    &\min f(\b{x}) + g(\b{z})\\
    &\bb{A}\b{x}+\bb{B}\b{z} = \b{0}
  \end{aligned}
\end{equation}

待优化的问题由两个部分组成，通过约束黏在一起。ADMM的想法是我们可以每次固定一个变量优化另外一个，交替优化$\b{x}$和$\b{z}$。将这个想法实现出来的技巧就是增广拉格朗日函数。写出这个问题的增广拉格朗日函数形式：

\begin{equation}
  \begin{aligned}
    L(\b{x}, \b{z}, \b{\lambda}) &= f(\b{x}) + g(\b{z}) + \b{\lambda}^T \bb{W} (\bb{A}\b{x}+\bb{B}\b{z}) +  \frac{1}{2}\lVert \bb{A}\b{x}+\bb{B}\b{z} \rVert_{\bb{W}}^2\\
    & = f(\b{x}) + g(\b{z}) + \frac{1}{2}\lVert \bb{A}\b{x}+\bb{B}\b{z} + \b{\lambda} \rVert_{\bb{W}}^2 - \frac{1}{2} \lvert \b{\lambda} \rVert_{\bb{W}}^2
  \end{aligned}
\end{equation}

ADMM优化的方式与ALM类似，只不过ALM中无约束优化$\b{x}$的一步在ADMM中变成分别优化$\b{x}$和$\b{z}$。于是我们可以得到下面的迭代形式：

\begin{equation}
  \begin{aligned}
    \b{x}^{l+1} &\gets \min f(\b{x}) + \frac{1}{2}\lVert \bb{A}\b{x}+\bb{B}\b{z}^l + \b{\lambda}^l \rVert_{\bb{W}}^2 \\
    \b{z}^{l+1} &\gets \min g(\b{z}) + \frac{1}{2}\lVert \bb{A}\b{x}^{l+1}+\bb{B}\b{z} + \b{\lambda}^l \rVert_{\bb{W}}^2 \\
    \b{\lambda}^{l+1} &\gets \bb{A}\b{x}^{l+1}+\bb{B}\b{z}^{l+1} + \b{\lambda}^l
  \end{aligned}
\end{equation}

这样交替优化原问题的好处是什么？理论上我们可以直接将变量组合在一起定义$\b{y}=[\b{x},\b{z}]$，然后直接求解$\b{y}$的优化问题，但是这样问题的规模就会扩大。如果单独关于$f(\b{x})$或者$g(\b{z})$的优化问题有好的性质，比于可以并行求解，或者Hessian矩阵固定，我们就可以在ADMM中利用这个性质，达到更快的收敛速度；而如果当成一个整体求解，往往不能利用这些性质进行优化。从另一个角度看，如果一个优化问题可以方便拆成两个部分$f(\b{x})+g(\b{x})$，我们就可以将其改写为：
$$
  \begin{aligned}
    &\min f(\b{x}) + g(\b{z})\\
    &\b{x}-\b{z} = \b{0}
  \end{aligned}
$$
从而使用ADMM快速求解。

## ADMM $\supseteq$ PD

<div class="text-center rounded-lg bg-green-50 dark:bg-gray-800">
  ADMM ⊇ Projective Dynamics: Fast Simulation of General Constitutive Models
  <a href="https://www-users.cse.umn.edu/~narain/files/admm-pd.pdf">
    <div class="i-carbon-document-pdf text-blue-500"/>
  </a>
  <br/>
  Projective Dynamics: Fusing Constraint Projections for Fast Simulation
  <a href="https://www.projectivedynamics.org/projectivedynamics.pdf">
    <div class="i-carbon-document-pdf text-blue-500"/>
  </a>
</div>

用隐式欧拉法模拟弹性体动力学可以化归为下面的Incremental Potential的优化问题：

\begin{equation}
  \begin{aligned}
    \min A(\b{q}) = \frac{1}{2h^2}\lVert \b{q} - \b{s} \rVert_{\bb{M}}^2 + E(\b{q})
  \end{aligned}
\end{equation}

其中$\b{q}$是整个系统的自由度，$\b{s}=\b{q}^n + h\b{v}^n + h^2\bb{M}^{-1}\b{f}_{ext}$，前面对应惯性项，后面对应势能项。$A(\b{q})$自动就被分成两个部分。惯性项是一个对角的二次型，可以很方便地优化。势能项一般可以写为求和的形式$E(\b{q})=\sum_i E_i(\bb{D}_i\b{q})$：在弹簧质点系统中，求和对弹簧进行，$\bb{D}_i\b{q}=\b{q}_{i1}-\b{q}_{i2}$，也就是弹簧两端点间的位矢；在FEM中，求和对每个四面体进行，$\bb{D}_i\b{q}=vec(\bb{F}_i)$，然后带入连续介质模型得到每个四面体的能量。这个性质说明势能项的优化可能可以并行进行。基于以上观察，Incremental Potential可以使用ADMM进行优化：

\begin{equation}
  \begin{aligned}
    &\min \frac{1}{2h^2}\lVert \b{q} - \b{s} \rVert_{\bb{M}}^2 + \tilde{E}(\b{p})\\
    &\bb{D}\b{q}-\b{p} = \b{0}
  \end{aligned}
\end{equation}

其中$\tilde{E}(\b{p})=\sum_i E_i(\b{p_i})=\sum_i E_i(\bb{D}_i\b{q})$。得到的迭代算法如下：

\begin{equation}
  \begin{aligned}
    \b{q}^{l+1} &\gets \min \frac{1}{2h^2}\lVert \b{q} - \b{s} \rVert_{\bb{M}}^2 + \frac{1}{2}\lVert \bb{D}\b{q}-\b{p}^l + \b{\lambda}^l \rVert_{\bb{W}}^2 \\
    \b{p}^{l+1} &\gets \min \tilde{E}(\b{p}) + \frac{1}{2}\lVert \bb{D}\b{q}^{l+1} - \b{p} + \b{\lambda}^l \rVert_{\bb{W}}^2 \\
    \b{\lambda}^{l+1} &\gets \bb{D}\b{q}^{l+1} - \b{p}^{l+1} + \b{\lambda}^l
  \end{aligned}
\end{equation}

拆开来看，关于$\b{q}$的优化问题是两个对角二次型相加的形式，因此有固定的Hessian矩阵$\bb{H} = \frac{1}{h^2}\bb{M}+\bb{D}^T\bb{W}\bb{D}$，可以很方便做预分解来加速运算。关于$\b{p}$的优化问题可以拆分开来：

$$
\sum_i E_i(\b{p}_i) + \frac{1}{2}\lVert \b{p}_i - (\bb{D}_i\b{q}^{l+1} + \b{\lambda}^l_i) \rVert_{\bb{W}}^2 
$$

显然这个问题可以并行求解。对每个$\b{p}_i$我们只需要求解一个小规模（弹簧质点中3DOF，FEM中9DOF）的优化问题，一般情况下少数几个（<10）L-BFGS迭代就能差不多收敛。对于特殊的能量形式还有更好的求解方法，比如论文的后面作者在PD的能量形式下证明了ADMM$\approx$PD。虽然PD的算法和ADMM很像，都有Global Step和Local Step，但是二者还是有不同的地方。ADMM的做法是将惯性项和势能项分开进行求解，势能项是并行优化的，$\b{p}_i$表示的是每个部分的形变，最终需要靠$\b{\lambda}_i$粘起来，迭代到后面得到一个全局光滑的形变。而PD的做法是将势能项写成二次距离项和约束：

$$
E(\b{q}) = \min_{\b{p}} \frac{\omega}{2} \lVert \bb{A}\b{q} - \bb{B}\b{p} \rVert^2 + \delta_{\bb{C}}(\b{p}) = \min_{\b{p}\in \bb{C}} \frac{\omega}{2} \lVert \bb{A}\b{q} - \bb{B}\b{p} \rVert^2
$$

然后将其中的距离项与惯性项一起求解，因为这部分都是二次的，所以有固定Hessian可以做预分解。剩下的约束项并行求解。可以看到PD求解约束的方式也不是ADMM使用的增广拉格朗日函数的形式。从收敛上来看，PD对应的是Quasi-Newton的收敛速度，ADMM的收敛则依赖于权重的选择。原论文中并**没有**关于收敛性的理论分析，但是给出了选择权重$\bb{W}$的一般性准则：当$\bb{W}$接近势能的Hessian，比如PD中的$\omega$时，能够达到不错（与PD相同）的收敛效率；当进一步减少权重收敛速度会更快，但是过于小的权重会导致系统不收敛。

## 摩擦碰撞

<div class="text-center rounded-lg bg-green-50 dark:bg-gray-800">
  Simple and Scalable Frictional Contacts for Thin Nodal Objects
  <a href="http://gdaviet.fr/files/hardContacts.pdf">
    <div class="i-carbon-document-pdf text-blue-500"/>
  </a>
</div>

![](/blogs/signorini-friction.png)

Signorini-Coulomb摩擦给出了碰撞点附近的相对速度$\b{u}$和接触力$\b{r}$应该满足的关系：

\begin{equation}
  \begin{aligned}
    0 \leq \b{u}_N &\perp \b{r}_N \geq 0 \\
    \b{r} \in K_{\mu} &\text{, if } \b{u}_T = 0 \\
    \b{r}_T = - \mu \b{r}_N \frac{\b{u}_T}{\lVert \b{u}_T \rVert} &\text{, if } \b{u}_T \neq 0
  \end{aligned}
\end{equation}

简记为$(\b{u}, \b{r})\in C_\mu$。这组约束比较难处理，主要是因为存在互补条件。将这组条件加入到弹性体的Incremental Potential的优化中，就可以得到带摩擦碰撞的弹性体动力学方程：

\begin{equation}
  \begin{aligned}
    \frac{\partial}{\partial \b{v}} A(\b{v}) &= \bb{B}^T\b{r} \\
    \b{u} &= \bb{B}\b{v} + \b{k} \\
    (\b{u}, \b{r}) &\in C_\mu
  \end{aligned}
\end{equation}

这组方程进行很多符号的简化，但是并不难理解。$A(\b{v})$是用速度改写的Incremental Potential：$A(\b{v})=\frac{1}{2}\lVert \b{v} - (\b{v}^n+h\bb{M}^{-1}\b{f}_{ext}))\rVert_\bb{M}^2 + E(\b{q}^n + h\b{v})$，$\bb{B}\b{v}+\b{k}$表示的是自由度速度到碰撞点速度的映射关系（我们假设碰撞点的法向、相对位置在优化中都是常量，$\b{k}$表示可能存在的与Kinematic的物体的碰撞的贡献），$\b{u}$和$\b{r}$表示的都是所有碰撞点速度和接触力的集合。一般我们迭代更新$\mu{v}$，每步迭代求解下面的二次约束问题：

\begin{equation}
  \begin{aligned}
    \bb{A}^k \b{v}^{k+1} &= \bb{A}^{k}\b{v}^k- \frac{\partial}{\partial \b{v}} A(\b{v}^k) + \bb{B}^T\b{r}\\
    \b{u} &= \bb{B}\b{v}^{k+1} + \b{k} \\
    (\b{u}, \b{r}) &\in C_\mu
  \end{aligned}
\end{equation}

这个问题比较难解，在刚体里有方法会使用离散摩擦锥的模型转化为LCP问题求解。但是因为$\bb{A}$的结构比较复杂，计算效率还是很慢。

难以优化的主要原因是约束$C_\mu$中存在互补条件，manifold的形状比较复杂。这篇文章一个核心贡献，就是放松这个约束变成Proxy convex friction law，从而变成一个凸优化的问题，进而使用ADMM快速求解。转化出来的形式如下：

\begin{equation}
  \min_{\bb{B}\b{v}+\b{k}\in K_{\frac{1}{\mu}}} A(\b{v})
\end{equation}

原文章把这一部分的证明放在了Appendix里，但这一部分其实对理解文章非常关键。这里我们首先引入一些凸优化的基本概念，再从这个形式倒推看看等价形式是什么。

我们定义一个凸集$C$的normal cone为$N_C(\b{x}) := \{\b{z}\in \mathbb{R}^n | \b{z}\cdot (\b{y} - \b{x}) \leq 0, \forall \b{y} \in C\}$，下图画出了$\b{x}$在$C$的边界和内部的两种情况。

<div class="w-120 mx-auto">
  <img src="/blogs/normal-cone.jpg"/>
</div>

有了normal cone的概念之后，我们可以给出**可微凸函数**$f(\b{x})$在**凸集**$C$上取最小值的等价描述：

$$\tilde{\b{x}}=\min_{\b{x}\in C}f(\b{x}) \Longleftrightarrow \nabla f(\tilde{\b{x}})\in -N_C(\tilde{\b{x}})$$

对照上图的两种情况，也不难理解这个形式：如果最小值在边界，负梯度应该朝外；如果最小值在内部，梯度为0。在一种特殊情况下，如果凸集$C$是摩擦锥$K_\mu$，我们有如下额外的结论：

$$\b{y} \in -N_{K_\mu}(\b{x}) \Longleftrightarrow K_\mu \ni \b{x} \perp \b{y} \in K_{1/\mu} \Longleftrightarrow \b{x} \in -N_{K_{1/\mu}}(\b{y})$$

我们可以按下图分情况验证这个结论的正确性。

<div class="w-150 mx-auto">
  <img src="/blogs/dual-cone.jpg"/>
</div>

如果$\b{x}=0$，画出normal cone发现$\b{y}$在$K_{1/\mu}$内；如果$\b{x}$在$K_\mu$的边上，$-N_{K_\mu}(\b{x})$ 也是$K_{1/\mu}$的边；如果$\b{x}$在$K_\mu$内部，则有$\b{y} = 0$。于是从左边可以推到中间。再根据对称性就能推到右边。在这两个结论的基础上，我们就能给出Proxy convex friction law的等价形式：

\begin{equation}
  \begin{aligned}
    &\min_{\bb{B}\b{v}+\b{k}\in K_{\frac{1}{\mu}}} A(\b{v}) \\
    \Leftrightarrow & \nabla A(\b{v}) \in -\bb{B}^TN_{K_{1/\mu}}(\bb{B}\b{v}+\b{k}) \\
    \Leftrightarrow & K_{1/\mu} \ni \bb{B}\b{v}+\b{k} \perp \nabla A(\b{v}) \in \bb{B}^T K_\mu \\
    \Leftrightarrow & \exist \b{r} \in K_\mu, \nabla A(\b{v}) = \bb{B}^T \b{r}, \b{r} \perp \bb{B}\b{v}+\b{k} \in K_{1/\mu}
  \end{aligned}
\end{equation}

将这个形式对照原问题，我们发现首先我们假设$A(\b{v})$是凸函数，而$A(\b{v})$一般非凸。这个问题比较好解决，如果我们按照一般的牛顿法迭代求解$\b{v}$，每步迭代中$A(\b{v})$都是近似原问题的凸二次函数。我们关于$\b{r}$的约束与原问题相同，问题在于我们给相对速度$\b{u}=\bb{B}\b{v}+\b{k}$多加了一个$K_{1/\mu}$的约束，而一般情况下$\b{u}$只有$\b{u}_N\geq 0$的约束。于是Proxy convex friction law的形式并不完全等价于原问题，而是有更强的约束，得到的最优解也不对应原问题的最优解，但是最大的好处在于我们现在得到了一个凸优化的问题。

这个带约束的优化问题可以使用下面的ADMM方式求解：

\begin{equation}
  \begin{aligned}
    &\min_{\bb{B}\b{v}+\b{k}\in K_{\frac{1}{\mu}}} A(\b{v}) \\
    \Leftrightarrow & \min_{\b{v}} A(\b{v}) + C(\b{v}) \\
    \Leftrightarrow & \min_{\b{v}, \b{p}} A(\b{v}) + C(\b{p}), \b{p}-\b{v}=\b{0} \\
  \end{aligned}
\end{equation}

其中$C(\b{v})$是约束的指示函数，如果$\bb{B}\b{v}+\b{k} \in K_{1/\mu}$时取0，否则取正无穷。套用ADMM的框架得到下面的迭代算法：

\begin{equation}
  \begin{aligned}
    \b{v}^{l+1} &\gets \min A(\b{v}) + \frac{1}{2}\lVert \b{v} - (\b{p}^l + \b{\lambda}^l) \rVert_{\bb{W}}^2 \\
    \b{p}^{l+1} &\gets \min C(\b{p}) + \frac{1}{2}\lVert \b{p} - (\b{v}^{l+1} - \b{\lambda}^l) \rVert_{\bb{W}}^2 \\
    \b{\lambda}^{l+1} &\gets \b{p}^{l+1} - \b{v}^{l+1} + \b{\lambda}^l
  \end{aligned}
\end{equation}

这个迭代算法可以利用ADMM带来的优势，如果$A(\b{v})$是二次型关于$\b{v}$的优化可以预计算Hessian，关于$\b{p}$的优化可以看成把$\b{v}^{l+1} - \b{\lambda}^l$投影到$C$上。同时我们注意到约束$C$只在第二步出现，因此如果把$C$替换为真正的摩擦约束$C_\mu$，我们就应该能迭代得到**真正原问题的解**。此时第二步变成了：

\begin{equation}
  \begin{aligned}
    \bb{W}\b{p} &= \bb{W} (\b{v}^{l+1} - \b{\lambda}^l) + \bb{B}^T\b{r}\\
    \b{u} &= \bb{B}\b{p} + \b{k} \\
    (\b{u}, \b{r}) &\in C_\mu
  \end{aligned}
\end{equation}

到这里，我们经过一通数学推导得到了一个看起来跟原问题差不多的形式，唯一的不同在于原来的$\bb{A}$被替换成了$\bb{W}$，而这一点非常重要，因为$\bb{W}$是一个对角阵，这给我们的求解带来了很大方便。原论文给出了一个Projected Gauss-Seidel的求解方法。而如果我们进一步假设每一对碰撞只关联了一对节点，我们则能导出跟另一篇论文类似的Projected Jacobi的形式，从而可以并行求解。