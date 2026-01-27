from typing import List

class Solution:
    def bisect(self, nums, target):
        l = -1
        r = len(nums)
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        return r

    def maximumCount(self, nums: List[int]) -> int:
        idx_n = self.bisect(nums, 0)
        idx_p = self.bisect(nums, 1)
        return max(idx_n, len(nums)-idx_p)

if __name__ == "__main__":
    s = Solution()
    print(s.maximumCount(nums = [-2,-1,-1,1,2,3]))