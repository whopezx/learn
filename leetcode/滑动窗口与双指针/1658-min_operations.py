from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 这道题没做出来，参考灵茶山艾府题解
        # 找最小的操作数使nums的元素和等于x，反过来就是找最长的子数组使元素和大于sum(nums)-x

        ans = -1
        s = sum(nums)-x
        if s < 0:
            return -1
        num_sum = 0
        left = 0
        for right, num in enumerate(nums):
            num_sum += num
            while num_sum > s:
                num_sum -= nums[left]
                left += 1
            if num_sum == s:
                ans = max(ans, right - left + 1)
        return -1 if ans == -1 else len(nums)-ans

        # # 灵茶山艾府题解
        # target = sum(nums) - x
        # if target < 0:
        #     return -1  # 全部移除也无法满足要求
        #
        # ans = -1
        # s = left = 0
        # for right, x in enumerate(nums):
        #     s += x
        #     while s > target:
        #         s -= nums[left]
        #         left += 1  # 缩小子数组长度
        #     if s == target:
        #         ans = max(ans, right - left + 1)
        # return -1 if ans < 0 else len(nums) - ans


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(nums = [1,1,4,5,1,3], x = 5))