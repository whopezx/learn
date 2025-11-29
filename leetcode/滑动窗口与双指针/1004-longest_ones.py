from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # ans = 0
        # left = 0
        # one = 0
        # zero = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         one += 1
        #     elif nums[i] == 0:
        #         zero += 1
        #     while zero > k:
        #         if nums[left] == 1:
        #             one -= 1
        #         elif nums[left] == 0:
        #             zero -= 1
        #         left += 1
        #     ans = max(ans, one+zero)
        # return ans

        # 参考灵茶山艾府题解，好像没有变快，反而满了，不过内存占用少很多
        ans = left = cnt0 = 0
        for right, x in enumerate(nums):
            cnt0 += 1 - x  # 0 变成 1，用来统计 cnt0
            while cnt0 > k:
                cnt0 -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.longestOnes(nums = [0,0,0,0], k = 0))