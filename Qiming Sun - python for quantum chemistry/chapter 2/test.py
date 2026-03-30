import sys
sys.path.append('../')
import time
import numpy as np
from utils.memory import MemoryMonitor

# # test 1
# # full_like()返回用第二个参数填充的array，这个array与第一个参数相同shape，相同type
# x = np.full_like([[1.2, 1.1]], 1e3)
# print(x)

# # test 2
# # TODO(WHB): 这里还需要进行详细的内存的测试
# x = np.array([10.0])
# a = np.array([1.0])
# b = np.array([1.0])
# for i in range(2000000):
#     x = np.sqrt(np.log(x/a)/b)
# print(x)
#
# for i in range(2000000):
#     np.sqrt(np.divide(np.log(np.divide(x, a, out=x), out=x), b, out=x), out=x)
# print(x)

# def search(a, eps=1e-9):
#     x = np.full_like(a, 1e3)
#     xlast = np.zeros_like(a)
#     while np.any(abs(x - xlast) > eps):
#         # 这种方式内存占用比下面的那种大
#         xlast = x
#         x = np.sqrt(np.log(x/eps)/a)
#
#         # xlast, x = x, np.sqrt(np.divide(np.log(np.divide(x, eps, out=xlast), out=xlast), a, out=xlast), out=xlast)
#     return x
#
# # monitor = MemoryMonitor()
# for i in range(1):
#     search(1.0)
# # peak = max(monitor.memory_buffer) / 1e6
# # print(f'memory use {peak} Mb')

# # test 3
# x = 1
# t0 = time.time()
# for i in range(100000000):
#     x += 1
# t1 = time.time()
# print(f"inplace operator use {t1-t0} s")  # 6.143 s
#
# x = 1
# t0 = time.time()
# for i in range(100000000):
#     x = x + 1
# t1 = time.time()
# print(f"ufunc operator use {t1-t0} s")  # 6.226 s
