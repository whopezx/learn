from typing import List
from collections import defaultdict


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums)-1
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for i in range(len(nums)):
            cnt[nums[i]] += 1
            while cnt[0] > 1:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(cnt[1], ans)
        return ans

        # # 下面这种方法耗时反而增加，灵茶山艾府的题解没使用哈希表，对于这种只有两种元素的nums
        # # 使用一个变量来维护确实会提高效率
        # ans = 0
        # left = 0
        # cnt = defaultdict(int)
        # for i in range(len(nums)):
        #     cnt[nums[i]] += 1
        #     while cnt[0] > 1:
        #         cnt[nums[left]] -= 1
        #         left += 1
        #     ans = max(cnt[1]+cnt[0]-1, ans)
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubarray(nums = [1,1,1]))