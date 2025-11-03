from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        ans = nums[k-1] - nums[0]
        for i in range(k, len(nums)):
            ans = min(ans, nums[i] - nums[i - k + 1])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumDifference(nums = [9,4,1,7], k = 2))