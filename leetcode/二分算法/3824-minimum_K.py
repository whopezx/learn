from typing import List
import math


class Solution:
    def minimumK(self, nums: List[int]) -> int:
        # 这里l和r可以继续优化，这个区间取得太大了
        l = 0
        r = sum(nums)

        t = 0
        while l+1<r:
            m = (l+r)//2
            for n in nums:
                t += math.ceil(n/m)
            if t <= m**2:
                r = m
            else:
                l = m
            t = 0
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.minimumK(nums = [1,1]))