from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans = max(ans, right-left+1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarrayLength(nums = [1,2,3,1,1,1,2,3,1,2], k = 2))