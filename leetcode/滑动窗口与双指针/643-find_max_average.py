from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])/k
        maxans = ans
        for i in range(k, len(nums)):
            ans += (nums[i] - nums[i-k])/k
            maxans = max(maxans, ans)
        return maxans
        # # 受到灵茶山艾府题解的启发，无需每次都计算平均值，只需要找到k个元素中的最大值然后最后除以k即可
        # ans = sum(nums[:k])
        # maxans = ans
        # for i in range(k, len(nums)):
        #     ans += nums[i] - nums[i-k]
        #     maxans = max(maxans, ans)
        # return maxans/k



if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage(nums = [5], k = 1))