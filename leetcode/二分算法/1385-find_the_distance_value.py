from typing import List


class Solution:
    def bisect(self, arr, target):
        l = -1
        r = len(arr)
        while l+1<r:
            m = (l+r)//2
            if arr[m] < target:
                l = m
            else:
                r = m
        return r

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        arr2.sort()
        for i in arr1:
            idx = self.bisect(arr2, i)
            if idx == len(arr2) and abs(i-arr2[idx-1]) > d:
                ans += 1
                continue
            if abs(i - arr2[idx-1]) > d and abs(i-arr2[idx])>d:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))