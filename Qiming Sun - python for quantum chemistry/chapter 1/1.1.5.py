# 使用conda也可以像'pip -m venv venvname'一样创建虚拟环境，实际上就是又创建了一个环境。
# 创建虚拟环境是为了有一个孤立的地方存程序依赖的包，
# 所以pip创建的虚拟环境也是类似于conda的一个一个的环境一样，因为pip实际上没有base

# conda建议全部使用conda安装包，但是有的包在anaconda中没有，就需要pip安装，
# 而pip安装的包，conda不能进行管理。所以书中建议常用的包，例如numpy，scipy等
# 使用conda安装，其他的包都用pip安装。