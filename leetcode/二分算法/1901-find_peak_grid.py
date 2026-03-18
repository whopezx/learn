from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # 查找最大值的方式不适用了，因为max(List[List])会比较每一行的第一个元素，但是最大值所在的那一行的第一个元素不一定是第一列中最大的

        # 灵茶山艾府题解
        left, right = -1, len(mat) - 1
        while left + 1 < right:
            i = (left + right) // 2
            mx = max(mat[i])
            if mx > mat[i + 1][mat[i].index(mx)]:
                right = i  # 峰顶行号 <= i
            else:
                left = i  # 峰顶行号 > i
        return [right, mat[right].index(max(mat[right]))]

        # # 思想上简单，但是算的慢
        # maxnum = 0
        # for i in range(len(mat)):
        #     if maxnum < max(mat[i]):
        #         maxnum = max(mat[i])
        #         maxx = i
        #         maxy = mat[i].index(maxnum)
        # return [maxx, maxy]


if __name__ == "__main__":
    s = Solution()
    print(s.findPeakGrid(mat = [[70,50,40,30,20],[100,1,2,3,4]]))