# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        depthLeft = 1 + self.maxDepth(root.left)
        depthRight = 1 + self.maxDepth(root.right)

        return max(depthLeft, depthRight)
