from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1  # 这里设为-1是为了把下标为0的位置包含进来
        r = len(nums)  # 这里设为数组长度是为了把最后一个元素后面的位置包含进来
        while l+1 < r:  # 这里用l+1是为了不会陷入死循环，因为下面更新l和m时，只是让l=m或r=m，而m是(l+m)//2，这永远不会让l大于等于m
            m = (l+r)//2  # 取中间靠左的位置，没什么好说的，二分法的做法
            if nums[m] < target:  # 更新左右界的判断，小于是查找连续相同元素靠左的位置，变成小于等于时，查找靠右的位置
                l = m  # 这里将l更新至m，即nums[m]还是在查找的区间内，即开区间
            else:
                r = m  # 同l=m
        return r  # 这种开区间写法，经过上面的更新后，需要查找的指标就是r

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert(nums=[1,3,5,6], target=0))