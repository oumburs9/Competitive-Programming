# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDif = 0
        def dfs(node, currMax, currMin):
            nonlocal maxDif
            if not node:
                return 
            
            currMax = max(currMax, node.val)
            currMin = min(currMin, node.val)
            maxDif = max(maxDif,currMax - currMin)

            dfs(node.left, currMax, currMin)
            dfs(node.right, currMax, currMin)

        dfs(root, root.val, root.val)
        return maxDif
        