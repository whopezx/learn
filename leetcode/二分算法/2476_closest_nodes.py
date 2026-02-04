from typing import List, Optional
from bisect import bisect_left


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestNodes(self, root: List[int], queries: List[int]) -> List[List[int]]:
        # 这里我不知道leetcode中的TreeNode数据类型怎么操作才能变成一个列表，所以我暂时直接传入一个列表
        root.sort()
        ans = []
        for q in queries:
            idx = bisect_left(root, q)
            if idx != len(root) and root[idx] == q:
                ans.append([root[idx], root[idx]])
            else:
                if idx == 0:
                    ans.append([-1, root[idx]])
                elif idx == len(root):
                    ans.append([root[idx-1], -1])
                else:
                    ans.append([root[idx-1], root[idx]])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.closestNodes(root = [1,2,4,6,9,13,14,15], queries = [2,5,16]))