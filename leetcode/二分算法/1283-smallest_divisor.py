from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # s = sum(nums)
        # nums_new = []
        # for n in nums:
        #     nums_new.append(s)
        # pass
        l = 0
        r = max(nums)
        s = 0
        while l+1<r:
            m = (l+r)//2
            for n in nums:
                s += math.ceil(n/m)
            if s<=threshold:
                r = m
            else:
                l = m
            s = 0
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.smallestDivisor(nums = [21212,10101,12121], threshold = 1000000))
