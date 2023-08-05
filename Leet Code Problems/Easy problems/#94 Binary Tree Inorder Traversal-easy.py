# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            # print left
            ans += self.inorderTraversal(root.left)
            
            # print root
            ans.append(root.val) 
            # print right
            ans += self.inorderTraversal(root.right)
        return ans

