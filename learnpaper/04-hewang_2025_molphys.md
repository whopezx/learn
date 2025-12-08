# 文章信息
这篇文章是提出使用XSF-TDA (spin-adapted spin-flip Tamm-Dancoff Approximation) 的文章。
由Hewang Zhao和Zhendong Li于2025年发表在Molcular Physics期刊上。
题目为，Spin-adapted open-shell time-dependent density functional theory:
towards a simple and accurate method for spin-flip-down excitations.

# 目标 or 创新
这篇文章主要就是把spin-adapted 用在SF-TDA上，然后计算一些结果来说明这个方法有用。

# 这篇文章给我写文章时带来的灵感
这篇文章在introduction首先说有哪些spin-flip方法，然后说了这些方法的缺点，即会存在自旋污染，并解释了为什么会有自旋污染，接着介绍了一些其他文章解决自旋污染的方法，最后给出这篇文章解决的方法。

在我的文章中可以先说目前实验中经常使用UTDDFT/UTDA来进行计算，然后说Unrestricted方法的缺点，即存在自旋污染并且耗时非常长，紧跟着就说为什么会有自旋污染和为什么耗时长，接着介绍RO方法解决了基态的自旋污染，但是即使基态使用ROKS，激发态也会存在自旋污染（参考[wiki](https://en.wikipedia.org/wiki/Spin_contamination)），再然后说明XTDA解决了自旋污染，不过对于实验中的分子耗时还是非常长，即使使用davidson对角化，所以发展sXTDA方法，最后总结一下sXTDA对某些体系的计算结果有偏差，但有的也会比XTDA的结果更好。
还要有一段来说明整个文章的结构，例如第二部分说了什么，第三部分说了什么等。并且还有ijab这些指标具体的含义，我觉得还有必要说明一下(ia|jb)是交换积分，(ij|ab)是库伦积分，与sTDA原始文章一致。

# Note
