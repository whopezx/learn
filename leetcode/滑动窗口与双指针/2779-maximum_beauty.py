from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        left = 0
        # for i in range(len(nums)):
        #     while nums[i] - nums[left] <= k:
        #         left -= 1
        #         if left < 0:
        #             break
        #     while nums[right] - nums[i] <= k:
        #         right += 1
        #         if right > len(nums)-1:
        #             break
        #     ans = max(ans, right-left-1)
        #     left = i
        #     right = i+1
        for i in range(len(nums)):
            while nums[i]-nums[left]>2*k:
                left += 1
            ans = max(ans, i-left+1)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maximumBeauty(nums = [49,26], k = 12))
