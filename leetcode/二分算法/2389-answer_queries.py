from typing import List


class Solution:
    def bisect(self, nums, target):
        l = -1
        r = len(nums)
        while l+1 < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m
            else:
                r = m
        return r

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        # 这里计算前缀和，参考灵茶山艾府题解
        # nums_c = []
        # for i in range(len(nums)):
        #     nums_c.append(sum(nums[:i+1]))
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        # 这里记录结果参考灵茶山艾府题解
        # ans = []
        # for i in queries:
        #     idx = self.bisect(nums, i)
        #     ans.append(idx)
        # return ans
        for i in range(len(queries)):
            queries[i] = self.bisect(nums, queries[i])
        return queries


if __name__ == "__main__":
    s = Solution()
    print(s.answerQueries(nums = [4,5,2,1], queries = [3,10,21]))