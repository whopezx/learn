from typing import List
from bisect import bisect_right


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def check(m):
            count = 0
            for i in range(len(nums)):
                idx = bisect_right(nums, nums[i]+m)-i-1
                count += idx
                if count >= k:
                    return True
            return False

        nums.sort()
        l = -1
        r = nums[-1] - nums[0]
        while l+1<r:
            m = (l+r)//2
            if check(m):
                r = m
            else:
                l = m
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.smallestDistancePair(nums = [1,1,1], k = 2))