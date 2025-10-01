from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == root.left+root.right:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkTree(TreeNode(10,4,6)))