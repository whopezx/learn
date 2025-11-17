from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        nums.sort()
        for i in range(len(nums)):
            while nums[i] > nums[left]*k:
                left += 1
            ans = max(i - left + 1, ans)
        return len(nums)-ans


if __name__ == '__main__':
    s = Solution()
    print(s.minRemoval(nums = [1,6,2,9], k = 3))