# Definition for a binary tree node.
from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        queue: Deque[Optional[TreeNode]] = deque()
        queue.append(root) 

        count = 0

        while len(queue) != 0:
            if count >= 2:
                return False
            addedToCount = False
            for _ in range(len(queue)):
                node = queue.popleft()   
                if node != None:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    if addedToCount == False:
                        count += 1
                        addedToCount = True

        return True
