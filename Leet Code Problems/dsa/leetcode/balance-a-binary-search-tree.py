# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(node):
            return inorder(node.left)+ [node.val]+ inorder(node.right) if node else  []
        
        def balance(vals):
            if not vals:
                return 

            mid = len(vals)//2

            node = TreeNode(vals[mid])
            node.left = balance(vals[:mid])
            node.right = balance(vals[mid+1:])
           
            return node
        
        inorder_vals = inorder(root)
        
        return balance(inorder_vals)
