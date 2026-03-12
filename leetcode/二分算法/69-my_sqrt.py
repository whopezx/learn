import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # # 使用内置函数，不过题目要求不使用，所以还需要想一下另外的方法
        # return math.floor(math.sqrt(x))
        if x == 1 or x == 0:
            return x
        l = 1
        r = x//2+1
        while l+1<r:
            m = (l+r)//2
            if m*m <= x:
                l = m
            else:
                r = m
        return l


if __name__ == "__main__":
    s = Solution()
    for i in range(10):
        print(s.mySqrt(x = i))