from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # if k <= 1:
        #     return 0
        ans = 0
        left = 0
        mul = 1
        for i in range(len(nums)):
            mul *= nums[i]
            while mul >= k and left <= i:
                mul /= nums[left]
                left += 1
            ans += i-left+1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.numSubarrayProductLessThanK(nums = [1,2,3], k = 0))

