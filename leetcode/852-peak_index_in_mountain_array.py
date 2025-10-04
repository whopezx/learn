from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))



if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray(arr = [0,2,1,0]))