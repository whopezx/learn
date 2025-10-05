from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # return arr.index(max(arr))

        # 二分查找
        left = 0
        right = len(arr) - 2
        while left < right:
            mid = left + (right - left) // 2
            # 若有相同的peak，返回最左侧的peak，注意山坡不能有平坦的地方
            if arr[mid] >= arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
            # # 若有相同的peak，返回最右侧的peak
            # if arr[mid] <= arr[mid + 1]:
            #     left = mid + 1
            # else:
            #     right = mid
        return right



if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray(arr = [0,1,2,2,2,1,0]))