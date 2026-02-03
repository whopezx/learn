from typing import List
from bisect import bisect_right

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        idx_l = 0
        while True:
            idx_r = bisect_right(arr, arr[idx_l])
            if idx_r-idx_l > len(arr)/4:
                return arr[idx_l]
            idx_l = idx_r

if __name__ == "__main__":
    s = Solution()
    print(s.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))