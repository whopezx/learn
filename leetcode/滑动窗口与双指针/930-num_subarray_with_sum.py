from typing import List

class Solution:
    # def biggerGoal(self, nums, goal):
    #     ans = 0
    #     left = 0
    #     sum_nums = 0
    #     for i in range(len(nums)):
    #         sum_nums += nums[i]
    #         while sum_nums >= goal and left <= i:
    #             sum_nums -= nums[left]
    #             left += 1
    #         ans += left
    #     return ans
    #
    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    #     ans0 = self.biggerGoal(nums, goal)
    #     ans1 = self.biggerGoal(nums, goal+1)
    #     return ans0-ans1

    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    #     ans = 0
    #     left1 = 0
    #     left2 = 0
    #     sum_nums1 = 0
    #     sum_nums2 = 0
    #     for i in range(len(nums)):
    #         sum_nums1 += nums[i]
    #         sum_nums2 += nums[i]
    #         while sum_nums1 >= goal and left1 <= i:
    #             sum_nums1 -= nums[left1]
    #             left1 += 1
    #         while sum_nums2 >= goal+1 and left2 <= i:
    #             sum_nums2 -= nums[left2]
    #             left2 += 1
    #         ans += left1 - left2
    #     return ans

    def smallerGoal(self, nums, goal):
        ans = 0
        left = 0
        sum_nums = 0
        for i in range(len(nums)):
            sum_nums += nums[i]
            while sum_nums > goal and left <= i:
                sum_nums -= nums[left]
                left += 1
            ans += i - left + 1
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans0 = self.smallerGoal(nums, goal)
        ans1 = self.smallerGoal(nums, goal-1)
        return ans0 - ans1

if __name__ == '__main__':
    s = Solution()
    print(s.numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))
    # [1,2,3,4,5,6,7,8,9], 8