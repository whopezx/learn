import sys
import importlib

# 动态调用库，这样做的好处是灵活，可以在程序运行过程中调用（但是我试了一下，在程序中直接import也是没问题的）。
# 但是这样调用还有缺点，由于这样调用一般不写在文件的开头，导致可读性变差，
# 并且在使用一些静态分析的库（pylint）分析带有这类导入的代码时，可能会有问题
np = importlib.import_module('numpy')  # same effect with 'import numpy as np' , note not same with 'import'
print(np.array([1,2,3]))
func_obj = getattr(np, 'array')
print(func_obj([4,5,6]))
