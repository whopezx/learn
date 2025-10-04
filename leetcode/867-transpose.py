from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # import numpy
        # return numpy.array(matrix).T.tolist()
        ans = []
        for i in range(len(matrix[0])):
            ans.append([])
        for row in matrix:
            for i in range(len(row)):
                ans[i].append(row[i])
        return ans




if __name__ == '__main__':
    s = Solution()
    print(s.transpose(matrix = [[1,2,3],[4,5,6]]))