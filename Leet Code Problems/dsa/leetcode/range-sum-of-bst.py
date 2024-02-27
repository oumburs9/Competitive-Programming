# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        _rangeSum = 0
        def dfs(node,low,high):
            nonlocal _rangeSum
            if not node:
                return 0


            if low <= node.val <= high:
                _rangeSum += node.val

            dfs(node.right,low,high)
            dfs(node.left,low,high)

        dfs(root,low,high)
        
        return _rangeSum

        