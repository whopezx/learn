from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        ans = len(nums)
        left = 0
        sumnum = 0
        for i in range(len(nums)):
            sumnum += nums[i]
            while sumnum >= target:
                sumnum -= nums[left]
                # if sumnum < target:
                ans = min(i - left + 1, ans)
                left += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))