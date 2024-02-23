# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def getSubtree(root):
            if root is None:
                return None
            
            new_root = TreeNode(root.val)
            new_root.left = getSubtree(root.left)
            new_root.right = getSubtree(root.right)
            return new_root

        if root is None:
            return None
        
        if root.val == val:
            return getSubtree(root)
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
