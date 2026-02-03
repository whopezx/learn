from typing import List
from bisect import bisect_right

class Solution:
    def bisect(self, nums, target):
        l = -1
        r = len(nums)
        while l+1 < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m
            else:
                r = m
        return r

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        length = len(potions)
        success -= 1
        for s in spells:
            idx = self.bisect(potions, success//s)  # 这里调用库函数bisect_right会计算的更快
            ans.append(length - idx)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))