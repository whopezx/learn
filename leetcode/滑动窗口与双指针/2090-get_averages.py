from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if 2*k+1 > len(nums):
            return [-1]*len(nums)
        ans = [-1]*k
        mean_ans = sum(nums[:2*k+1])
        ans.append(mean_ans//(2*k+1))
        for i in range(2*k+1,len(nums)):
            mean_ans += nums[i] - nums[i-2*k-1]
            ans.append(mean_ans//(2*k+1))
        for i in range(k):
            ans.append(-1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getAverages(nums = [8], k = 100000))