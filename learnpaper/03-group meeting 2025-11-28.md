# 文章信息
两篇文章用于讲大组会的文章（老师发给我的）。

1. 由Yizhe Chen于2025年发表在JOURNAL OF THE AMERICAN CHEMICAL SOCIETY上。
题目为Charge-Transfer States Enable Spin-Selective Formation of Quartet
State Qudits in Luminescent Radical-Chromophore Dyads
2. 由Yoshio Teki于2025年发表在JOURNAL OF THE AMERICAN CHEMICAL SOCIETY上。
题目为Multispin Photoexcited State and Generation of Dynamic Electron
Spin Polarization Observed in Anthracene−Radical-Linked Systems
with Extended π‑Conjugated Spin Coupler


# 目标 or 创新
这篇文章制作了比较纯的四重态初始态，并且通过一些光谱来验证了中间涉及到的一些过程，给通过分子工程设计纯的初始态提供了思路。

# Note
32 主要看看里面有什么不清楚的问题 理论是否有可能帮助解释 之前我跟崔老师聊过 可以考虑结合bdf或pyscf做非绝热动力学研究 但还需要实现nac 以及做和动力学程序的接口

33 跟上次那个类似也是研究d-q动力学的 组会时一起简单讲一下 看看里面有什么问题 我们后面能不能用xtddft结合非绝热动力学研究

---

第一篇：

为什么用四重态

电子顺磁共振如何揭示

CT（电荷转移）动力学上胜过EnT（能量转移），如何通过动力学来看出

结论中没观测到EnT的现象，那EnT应该是什么样的

三重态的发色团和自由基的自旋哈密顿中spin exchange coupling大于其他的相互作用，
这两种体系的自旋混合会得到四重态的体系，
什么是spin exchange coupling，什么是自旋混合

动力学方程

为什么电荷会转移/重组呢，什么导致了这种现象

---

摘要中提到瞬态光谱可以指出TTM-发色团在光激发下电荷从TTM转移到NDI，这个过程CT动力学上胜过EnT。
电子顺磁共振光谱指出自旋轨道耦合电荷转移系间窜越会生成三重态的NDI，和二重态的TTM混合形成四重态。

系间窜越，自旋轨道电荷转移系间窜越（闭壳层常见，32中的38-43引文）

Result And Discussion
第一段讲了TTM和DNI的结合位点，并通过瞬态吸收光谱来说明确实是在这个位点结合。并且通过瞬态光谱说明经过光激发二重态的TTM和经过光激发单重态的DNI在不同环境温度下也是比较稳定的。
这里也说明了TTM和NDI之间的相互作用是比较弱的，为使用Marcus理论解释生成TTM阳离子和NDI阴离子做铺垫。

第二段讲了使用Weller equation来说明存在电荷转移，利用循环伏安法，电化学测量得到一些量，代入方程计算，$E_{CT}=1.75$eV，说明会有一个驱动力让电荷从经过光激发的二重态TTM分离出来。

第三段讲了通过瞬态吸收光谱看到了二重态的TTM+离子和单重态的NDI-离子，并且这两个离子的产率达到99%，并且在298K没有看到三重态的NDI，最后给出结论EnT没有发生。

第四段最后结论有点没看懂，这一段讲了随着温度的降低，瞬态吸收光谱的一些特征没变，但是中间体出现的时间持续增长，即CS和CR的速率常数变了，并且在85K时出现了三重态的NDI，也就是说charge recombination在低温减弱（在高温时没有三重态的NDI）。在低温出现三重态NDI的原因是玻璃态PrCN中缓慢的溶剂重组动力学，使得CT态在快速电子转移事件的时间尺度上不稳定。

第六段讲了使用plus-EPR光谱测量，通过LMD的光谱可以说明在85K下二重态TTM和三重态NDI会发生强烈的交换耦合。

第七段讲了使用章动实验并结合公式二，可以说明确实产生了四重态

第八段讲了要通过SOCT-ISC来解释出现四重态现象的原因。并且使用TREPR来给出SOCT-ISC中需要的一些量。
最后给出了一个理论上的哈密顿量。

第九段解释了哈密顿量中的一些符号的含义，和TREPR测量的量对应公式中哪个符号，

---

