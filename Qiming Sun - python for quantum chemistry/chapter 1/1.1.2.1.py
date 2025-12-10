import sys
print(sys.path)
a = 1

# 打印sys.path
# [
#     '/mnt/d/Master/learn/master/Qiming Sun - python for quantum chemistry/chapter 1',
#     '/home/whope/miniconda3/envs/pfqc/lib/python310.zip',
#     '/home/whope/miniconda3/envs/pfqc/lib/python3.10',
#     '/home/whope/miniconda3/envs/pfqc/lib/python3.10/lib-dynload',
#     '/home/whope/miniconda3/envs/pfqc/lib/python3.10/site-packages'
# ]
# 其中搜索的顺序确实是
# 1.当前文件夹
# 2.pythonpath（第三行的路径）
# 3.site-packages文件夹
# 4.由于我这里暂时没有使用pip install -e安装的包，所以路径中sys.path中暂时没有.pth中的路径。

# 我这里查看了site-packages文件夹，这个文件夹在每个人的环境下面可以找到，
# 即/path/to/your/envs/lib/python3.X/site-packages
# 其中包含了所有通过pip install安装的包
