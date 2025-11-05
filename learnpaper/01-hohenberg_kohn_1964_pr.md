# 文章信息
这篇文章是提出使用电子密度泛函的原始文章。
由Pierre Hohenberg和Walter Kohn于1964年发表在Physical Review期刊上。
题目为，Inhomogeneous Electron Gas.

# 目标 or 创新
这篇文章以计算不均匀电子气为模型，说明使用一个任意泛函$F[n(r)]$可以表示电子气的基态能量。

# Note
文章分为三个部分，接下来一块一块说明。

第一部分主要说明了后面我们称之为**Hohenberg-Kohn定理**的内容，即**Hohenberg-Kohn第一定理：外势$v(r)$是电子密度$n(r)$的唯一泛函**和**Hohenberg-Kohn第二定理：给定基态电子密度后就可以确定基态能量**。下面先简单介绍一下，然后给出定理的证明。

首先使HK第一定理，
$n(r)$是$v(r)$的泛函是明显的。因为给定外势后，通过求解薛定谔方程可以得到对应的基态波函数$\Psi(r)$，即基态波函数和外势的关系为$\Psi[v(r)]$，而基态电子密度为
$$
    n(r)=\langle\Psi(r)|\psi^*(r)\psi(r)|\Psi(r)\rangle
$$
可以很明显的看出$n(r)$是$\Psi(r)$的函数。所以$n(r)$是$v(r)$的函数，即$n[v(r)]$。这个过程反过来逻辑是通顺的吗，即Hohenberg-Kohen第一定理，通过电子密度唯一确定外势。文中在第一部分通过反证法证明了这个逻辑是通顺的，接下来给出证明。需要注意，文中假设基态是不简并的。

首先假设同一电子密度$n(r)$对应两个不同的外势$v(r)$和$v'(r)$，并且这两个外势不止相差一个常数，即$v(r)-v'(r)\neq C$。如果这两个外势仅相差一个常数，只会导致两个外势对应的基态能量相差相同的常数$C$，而不会改变基态波函数。这两个外势对应各自的基态波函数为$\Psi(r)$和$\Psi'(r)$，对应各自的哈密顿算符为$H$和$H'$。接下来由于基态能量对应基态波函数，其他波函数计算能得到的能量都会高于基态能量，所以有下面的关系
$$
    E = \langle\Psi|H|\Psi\rangle 
    \lt \langle\Psi'|H|\Psi'\rangle
    = \langle\Psi'|H'-V'+V|\Psi'\rangle
    = \langle\Psi'|H'|\Psi'\rangle + \langle\Psi'|V-V'|\Psi'\rangle \\
    = E'+ \langle\Psi'|v(r)\psi^{*}(r)\psi(r) - v'(r)\psi^*(r)\psi(r)|\Psi'\rangle 
    = E'+\langle\Psi'|[v(r)-v'(r)]\psi^*(r)\psi(r)|\Psi'\rangle \\
    = E'+\int v(r)-v'(r)\langle\Psi'|\psi^*(r)\psi(r)|\Psi'\rangle dr
    = E'+\int [v(r)-v'(r)]n(r)dr
$$
其中$V=\int v(r)\psi^*(r)\psi(r)dr$是将外势算符表示为场算符的形式（gpt是这样解释的）。注意最后一行的第一个等号后面，基态波函数$\Psi'$的自变量可以不是$r$，所以$v(r)-v'(r)$可以移到狄拉克符号外面。所以根据上式可以得到下面的结论
$$
    E\lt E'+\int[v(r)-v'(r)]n(r)dr
$$
同理
$$
    E'=\langle\Psi'|H'|\Psi'\rangle\lt E+\int[v'(r)-v(r)]n(r)dr
$$
将上面两式相加得到
$$
    E'+E\lt E+E'
$$
这明显是错误的，所以假设不成立，即同一电子密度对应唯一的外势，HK第一定理得证。

然后是第二定理，首先定义通用泛函
$$
    F[n] = \langle\Psi|T+U|\Psi\rangle
$$
这个泛函和外场无关，所以当体系的电子密度确定时，这一项就是确定的。
进而能量的期望值可以写为
$$
    E = \langle\Psi|T+U+V|\Psi\rangle\\
    E = \langle\Psi|V|\Psi\rangle+F[n]\\
    E = \int v(r)n(r)dr + F[n]
$$
当电子数确定时，即
$$
    N[n] = \int n(r)dr = N
$$
基态的电子密度给出基态能量，即
$$
    E_v[\Psi] = \int v(r)n(r)dr+F[n] \lt \int v(r)n'(r)dr+F[n']
$$
实际上HK第二定理就是用电子密度的形式说了一下变分原理的结论。不过注意电子数守恒的限制条件一定要遵守，因为如果给定的电子密度的积分不是$N$而是$N-1$或$N+1$，有可能给出更低的能量，但这不是我们希望的结果。

由于库伦相互作用是长程相互作用，即在很远的距离也会有库伦相互作用，这一部分计算比较复杂，所以将这一部分从$F[n]$分离出来会简化后面的计算，将这一部分定义为$G[n]$，接下来通过推导给出将$G[n]$从$F[n]$分离出来后$F[n]$的形式
$$
\begin{aligned}
    F[n] &= \langle\Psi|T+U|\Psi\rangle\\
    &= \langle\Psi|\frac{1}{2}\int\nabla\psi^*(r)\nabla\psi(r)dr|\Psi\rangle + \langle\Psi|\frac{1}{2}\int\frac{1}{|r'-r|}\psi^*(r')\psi^*(r)\psi(r)\psi(r')drdr'|\Psi\rangle\\
    &= \frac{1}{2}\int\langle\Psi|\nabla\psi^*(r)\nabla\psi(r)|\Psi\rangle dr+\frac{1}{2}\int\frac{1}{|r'-r|}\langle\Psi|\psi^*(r')\psi^*(r)\psi(r)\psi(r')|\Psi\rangle drdr'\\
    &= \frac{1}{2}\int\left[\langle\Psi|\nabla_{r'}\psi^*(r')\nabla\psi(r)|\Psi\rangle|_{r'=r}\right] dr +\frac{1}{2}\int\frac{1}{|r'-r|}n_2(r'r;r'r)drdr'\\
    &= \frac{1}{2}\int\left[\nabla_{r'}\nabla_{r}\langle\Psi|\psi^*(r')\psi(r)|\Psi\rangle|_{r'=r}\right]dr + \frac{1}{2}\int\frac{n_2(r'r;r'r)-n_1(r;r)n_1(r';r')+n_1(r;r)n_1(r';r')}{|r'-r|}drdr'\\
    &= \frac{1}{2}\int \nabla_{r'}\nabla_{r} n_1(r';r)dr + \frac{1}{2}\int\frac{C_2(r'r;r'r)}{|r'-r|}drdr' + \frac{1}{2}\int\frac{n_1(r;r)n_1(r';r')}{|r'-r|}drdr'\\
    &= G[n] + \frac{1}{2}\int\frac{n_1(r;r)n_1(r';r')}{|r'-r|}drdr'
\end{aligned}
$$
其中$n_1$为前面定义的电子密度，$n_2(r'r;r'r)=\langle\Psi|\psi^*(r')\psi^*(r)\psi(r)\psi(r')|\Psi\rangle$，$C_2(r'r;r'r)=n_2(r'r;r'r)-n_1(r;r)n_1(r';r')$。在推导的过程中可以将求期望值与$del$算符换顺序，这是因为当被积函数或者被求导的函数是绝对连续时求导和积分可以换顺序，而场算符是单值，连续，平方可积的，所以可以换顺序。求期望值和积分换顺序则是直接的。这里实际上是把单体项提出来，然后后续只需要处理$G[n]$即可。根据上面的推导，$G[n]$的具体形式为
$$
    G[n] = \frac{1}{2}\int\left[\nabla_{r'}\nabla_{r} n_1(r';r)|_{r'=r}\right]dr + \frac{1}{2}\int\frac{C_2(r'r;r'r)}{|r'-r|}drdr'
$$
可以定义一个能量密度泛函$g_r[n]$ 
$$
    g_r[n]=\frac{1}{2}\nabla_{r'}\nabla_{r}n_1(r';r)|_{r'=r} + \frac{1}{2}\int\frac{C_2(r-r'/2;r+r'/2)}{|r'|}dr'
$$

因为$F[n]$是能量，进而$G[n]$也是一个能量，所以$g_r[n]$是能量密度。$g_r[n]$第一项很好理解，就是把积分号去掉了，第二项对自变量进行了一些变换，所以$C_2$的形式和前面给出的就不一样了。这里我仔细想了一下应该不是进行了坐标变换，因为进行坐标变换后积分元也是要变的，这样$g_r[n]$的第一项和第二项经过积分得到$G[n]$时，积分的变量就不一样了，不能仅仅通过$\int g_r[n] dr$得到$G[n]$，所以这里应该仅仅是在被积函数内部调整了一下自变量的形式。需要注意的是，$g_r[n]$加一个关于$n$的函数经过积分后也能够得到$G[n]$，即
<!-- 第二项对被积函数进行了坐标变换，但是积分元由于变换前后不会添加额外的变化，即$drdr'=dsdR$，所以还是将积分元写为$drdr'$， -->
$$
    \overline{g}_r[n]= g_r[n] + \sum_{i=1}^3 \frac{\partial}{\partial x_i}h_r^{(i)}[n]
$$
其中第二项经过对$r$的积分后是一个关于$n$的函数。所以对应于$G[n]$的能量密度泛函不止一个，而是一系列泛函。这应该就是能够发展出那么多不同的泛函的理论基础。

---

第二部分给出了一个具体的例子，在这个例子中首先给出具体的$G[n]$和$\overline{g}_r[n]$的形式。

这个例子是几乎均匀的电子气，所以电子密度可以定义为
$$
    n(r)=n_0+\tilde{n}(r)
$$
其中$\tilde{n}(r)$是一个微扰，满足$\tilde{n}(r)/n(r)<< 1$，并且有
$$
    \int \tilde{n}(r)dr = 0
$$
所以，利用泛函的泰勒展开有
$$
\begin{aligned}
    G[n]&=G[n_0+\tilde{n}(r)]\\
    &=G[n_0]+\int K(r)\tilde{n}(r)dr\\
    &+\int\int K(r;r')\tilde{n}(r)\tilde{n}(r')dr dr'\\
    &+\int\int\int K(r;r';r'')\tilde{n}(r)\tilde{n}(r')\tilde{n}(r'')drdr'dr''+\cdots
\end{aligned}
$$
其中$K$是不同阶的泛函导数$\frac{\delta^i G[n]}{\delta n(r_1)\cdots\delta n(r_i)}$。由于这里考虑几乎均匀的自由电子气，所以可以认为几乎没有外势，或者外势几乎均匀，进而可以近似认为体系是平移不变的。
平移不变性可以说明
$$
    G[n(r)] = G[n(r+R)]\quad \forall R
$$
而对某一点$r$加一个额外的扰动，$G[n(r+\Delta r)]$的变化都是相同的，这里可以按照导数的定义来理解，
$$
    \lim_{\Delta r\rightarrow 0 }\frac{G[n(r+\Delta r)]-G[n(r)]}{\Delta r}
$$
由于在任意一点加微小扰动，$G[n(r+\Delta r)]$都仅与$\Delta r$有关，则上式分子仅与$\Delta r$有关，除以$\Delta r$后仅剩一个常数，所以实际上一阶泛函导数为常数，所以
$$
    \int K(r)\tilde{n}(r)dr = \int C\ \tilde{n}(r)dr = C\int\tilde{n}(r)dr=0
$$
其中用到了几乎均匀电子气的约束$\int\tilde{n}(r)dr=0$