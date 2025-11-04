from typing import List
# from sortedcontainers import SortedDict  # 题解中有利用SortedDict进行计算的，不过要安装，所以暂时不考虑
"""后续再来看这道题，这道题里面有涉及到桶？后面再看一下什么是桶"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # 这种方法的时间复杂度为O(nk)，其中k为indexDiff的大小，在leetcode中运行会超时
        for i in range(len(nums)):
            for j in range(i+1, min(i+indexDiff+1, len(nums))):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3))