import sys

assert (3 , 9) < sys.version_info < (3 , 11)
# 主要版本号（major），次要版本号（minor），微型版本号（micro），发布级别（releaselevel），序列号（serial）
print(sys.version_info)  # sys.version_info(major=3, minor=10, micro=0, releaselevel='final', serial=0)
