from typing import List
from collections import defaultdict


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        l = -1
        for idx, p in enumerate(points):
            points[idx] = max(abs(p[0]), abs(p[1]))
        r = max(points)+1  # 这里加一是为了扩大边界
        ans = 0
        while l+1 < r:
            label = defaultdict(int)
            m = (l+r)//2
            for idx, p in enumerate(points):
                if p <= m:
                    label[s[idx]] += 1
                    if label.get(s[idx]) > 1:
                        break
            if len(label.values()) == 0:
                l = m
                continue
            maxlabel = max(label, key=label.get)  # 这里可以学习一下max函数的用法
            if label[maxlabel] < 2:
                l = m
            else:
                r = m
        for p in points:
            ans += p <= l
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxPointsInsideSquare(points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"))