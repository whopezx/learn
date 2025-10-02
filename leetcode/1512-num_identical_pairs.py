import collections
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        times = 0
        j = 1
        for ni in nums:
            for nj in nums[j:]:
                if ni == nj:
                    times += 1
            j += 1
        # # 除了上面的暴力解法，还有使用哈希表(python中字典的底层为hash表)的解法，计算复杂度为 O(n)，但空间复杂度也提高变为O(n)
        # m = collections.Counter(nums)
        # times = sum(v * (v - 1) // 2 for k, v in m.items())
        return times


if __name__ == '__main__':
    s = Solution()
    print(s.numIdenticalPairs([1,2,3,1,1,3]))