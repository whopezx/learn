from typing import List
from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target<=matrix[i][-1]:
                break
        idx = bisect_left(matrix[i], target)
        if idx == len(matrix[0]):
            return False
        return target == matrix[i][idx]


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix(matrix = [[1]], target = 0))