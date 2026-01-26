# 关于PEP8的标准，使用pylint，flake8或Ruff可以进行检测
# 在idea中可以集成这类工具，我这里不在pycharm中集成，现在pycharm占用太多内存，再添加这些工具，很容易崩溃。
# 我在pfqc环境中安装了pylint，直接pylint /path/to/your.code 即可检测，
# 检测也是比较严格的。下面是实例输出

# ************* Module 1.3.2
# 1.3.2.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# 1.3.2.py:1:0: C0103: Module name "2" doesn't conform to snake_case naming style (invalid-name)
# 1.3.2.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
# 
# -----------------------------------
# Your code has been rated at 0.00/10