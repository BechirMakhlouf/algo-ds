from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root == None:
    #         return 0
    #
    #     depthLeft = 1 + self.maxDepth(root.left)
    #     depthRight = 1 + self.maxDepth(root.right)
    #
    #     return max(depthLeft, depthRight)

    # def diameterOfBinaryTree(self, root: Optional[TreeNode], maxD=0) -> int:
    #     if root == None:
    #         return maxD
    #
    #     diameter = self.maxDepth(root.left) + self.maxDepth(root.right)
    #     maxD = max(maxD, diameter)
    #     return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode], maxCount = 0) -> int:
        if root == None:
            return 0
        return 1 + self.diameterOfBinaryTree(root.left)

        count += 1
        self.diameterOfBinaryTree(root.right)
        count -= 1

        return 0


s = Solution()
