from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # # 我第一个想到的就是这个方法
        # ans = [-1, -1]
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         ans[0] = i
        #         break
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] == target:
        #         ans[1] = i
        #         break
        # return ans

        # # 第二个方法使用python自身的二分查找库bisect
        # ans = [-1, -1]
        # ans[0] = bisect.bisect_left(nums, target)  # 如果nums中有target则返回靠左的位置
        # ans[1] = bisect.bisect_right(nums, target)  # 如果nums中有target则返回靠右的位置
        # if ans[0] == ans[1]:
        #     return [-1, -1]
        # else:
        #     return [ans[0], ans[1]-1]

        # 第三个方法就是自己写二分查找，不困难，灵茶山艾府推荐写都是开区间的程序，所以后续都是两边开区间的程序
        ans = [-1, -1]
        ans[0] = self.my_bisect_left_open(nums, target)
        ans[1] = self.my_bisect_left_open(nums, target+1)
        if ans[0] == ans[1]:
            return [-1, -1]
        else:
            return [ans[0], ans[1]-1]

    def my_bisect_left_close(self, nums, target):
        # 全闭区间写法，我先写了一个有问题的程序，然后参考灵茶山艾府题解修改
        # bisect_left和bisect_right的区别仅在while中if判断的符号是<还是<=
        # bisect_left的写法
        l = 0
        r = len(nums) - 1
        while l <= r:  # 这里用<会导致nums中为奇数数目的元素时有问题
            m = (l + r) // 2
            if nums[m] < target:
                # 这里加1有两个目的，else中的减1同样道理
                # （1）为了让左区间在目标值的右边，因为target比nums[m]大，
                # （2）当target比nums中最大的元素还大，不会陷入死循环
                l = m + 1
            else:
                r = m - 1
        return l

    def my_bisect_left_open(self, nums, target):
        # 全开区间写法，还有左闭右开这里不在展示
        # bisect_left和bisect_right的区别仅在while中if判断的符号是<还是<=
        # bisect_left的写法
        l = -1
        r = len(nums)
        while l+1 < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums = [5,7,7,8,8,10], target = 7))