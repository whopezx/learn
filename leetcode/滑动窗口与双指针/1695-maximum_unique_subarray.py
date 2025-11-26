from typing import List
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        tempans = 0
        left = 0
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            tempans += num
            while cnt[num] >= 2:
                cnt[nums[left]] -= 1
                tempans -= nums[left]
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans = max(ans, tempans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]))