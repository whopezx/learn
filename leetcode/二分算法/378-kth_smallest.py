import math
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # # 这里判断标准是有问题的，第一个测试设置k=5时就能看出来
        # diag = max(math.floor(math.sqrt(k))-2, 0)
        # l = matrix[diag][diag]
        # diag = math.ceil(math.sqrt(k))-1
        # r = matrix[diag][diag]
        l = min(min(matrix))-1
        r = max(max(matrix))
        while l+1 < r:
            m = (l+r)//2
            count = 0
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j]<=m:
                        count += 1
                    else:
                        break
            if count < k:
                l = m
            else:
                r = m
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
    # print(s.kthSmallest(matrix = [[5,8,11,11,12,12,14,14,19],[9,9,14,17,17,19,21,26,27],[12,15,15,21,21,26,30,35,36],[17,17,20,25,28,30,32,35,39],[20,21,22,29,30,32,34,36,43],[24,24,25,31,36,40,40,43,45],[28,31,32,36,36,45,49,53,56],[29,33,36,39,40,50,54,57,57],[34,36,37,41,42,53,55,58,59]], k = 67))