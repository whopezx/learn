from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = -1
        r = len(nums)-1
        while l+1 < r:
            m = (l+r)//2
            if nums[m] >= nums[m+1]:
                r = m
            else:
                l = m
        return r

        # # 最简单的写法，峰值一定是比两边都大的值，而返回哪个峰值都可以，那么我直接返回最大的峰值
        # # 而最大的峰值也就是最大的值，然后查找这个最大值的索引即可
        # return nums.index(max(nums))


if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement(nums = [1,2,1,3,5,6,4]))