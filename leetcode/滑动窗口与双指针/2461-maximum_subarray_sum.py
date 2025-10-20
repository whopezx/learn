from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        maxans = 0
        cnt = defaultdict(int)
        for i in range(len(nums)):
            ans += nums[i]
            cnt[nums[i]] += 1
            if i < k-1:
                continue
            if len(cnt) < k:
                ans -= nums[i-k+1]
                cnt[nums[i-k+1]] -= 1
                if cnt[nums[i-k+1]] == 0:
                    del cnt[nums[i-k+1]]
                continue
            maxans = max(maxans, ans)
            ans -= nums[i-k+1]
            del cnt[nums[i-k+1]]
        return maxans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumSubarraySum(nums = [4,4,4], k = 3))