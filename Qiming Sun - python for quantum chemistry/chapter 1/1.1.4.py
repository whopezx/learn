# 执行完'python -m venv new-env-dir'后，在当前目录出现了new-env-dir文件夹
# 接着使用'source new-env-dir/bin/activate'就可以激活虚拟环境。

# 直接输入'deactivate'就可以退出虚拟环境

# 如果不用这个虚拟环境了，直接delete这个虚拟环境的文件夹即可。

# 创建的虚拟环境并不能简单的通过'scp'或'mv'或'cp'移动到其他位置或机器再次运行程序。
# 所以通过创建requirements.txt，然后再在其他机器上安装环境来运行程序。
# 通过'pip freeze --local > requirements.txt'来生成requirements.txt，
# 使用1.1.1.3节提到的'pipreqs ./'生成，好像生成的是主要环境的requirements.txt
# 也可能是在虚拟环境中没安装pipreqs包导致的，可以再测试一下，好像不是，这个不是很好用。
# 没有'pip freeze ......'的命令好用