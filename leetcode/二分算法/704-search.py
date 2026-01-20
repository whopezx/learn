from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while l+1 < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m
            else:
                r = m
        if r == len(nums) or nums[r] != target:
            return -1
        else:
            return r

if __name__ == '__main__':
    s = Solution()
    print(s.search(nums = [-1,0,3,5,9,12], target = 3))