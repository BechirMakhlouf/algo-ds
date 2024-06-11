from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     def findDepth(root: Optional[TreeNode]) -> int:
    #         if root == None:
    #             return 0
    #         depthRight =  1 + findDepth(root.right)
    #         depthLeft =  1 + findDepth(root.left)
    #         return max(depthLeft, depthRight)
    #
    #     def findMaxDiameter(root:Optional[TreeNode], maxDiameter=0) -> int:
    #         if root == None:
    #             return maxDiameter
    #         diameter = findDepth(root.left) + findDepth(root.right)
    #         maxDiameter = max(maxDiameter, diameter)
    #         return max(findMaxDiameter(root.left, maxDiameter), findMaxDiameter(root.right, maxDiameter))
    #         
    #     return findMaxDiameter(root)
    def diameterOfBinaryTree(self, root: Optional[TreeNode], maxD=0) -> int:
        if root == None:
            return maxD

        maxDLeft = 1 + self.diameterOfBinaryTree(root.left, maxD)
        maxDRight = 1 + self.diameterOfBinaryTree(root.right, maxD)
        return max(maxDLeft, maxDRight) -1
