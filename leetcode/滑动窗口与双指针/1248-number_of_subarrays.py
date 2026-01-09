from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans0 = self.biggerk(nums, k)
        ans1 = self.biggerk(nums, k+1)
        return ans0-ans1

    def biggerk(self, nums, k):
        ans = 0
        left = 0
        odd_nums = 0
        for i in range(len(nums)):
            odd_nums += nums[i]%2
            while odd_nums >= k:
                odd_nums -= nums[left]%2
                left += 1
            ans += left
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))