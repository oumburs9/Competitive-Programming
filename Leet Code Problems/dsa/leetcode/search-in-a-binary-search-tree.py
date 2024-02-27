# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def buildSubTree(node):
            if not node:
                return None
            
            newNode = TreeNode(node.val)
            newNode.left = buildSubTree(node.left)
            newNode.right = buildSubTree(node.right)

            return newNode
        
        if not root:
            return None
            
        if root.val == val:
            return buildSubTree(root)

        elif root.val > val:
            return self.searchBST(root.left,val)
        
        elif root.val < val:
            return self.searchBST(root.right,val)