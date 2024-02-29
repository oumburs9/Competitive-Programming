# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0
        
        def dfs(node):
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            leftValid, leftMin, leftMax, leftSum = dfs(node.left)
            right_valid, right_min, rightMax, rightSum = dfs(node.right)
            
            if leftValid and right_valid and leftMax < node.val < right_min:
                currentSum = leftSum + rightSum + node.val

                self.maxSum = max(self.maxSum, currentSum)
                
                return True, min(leftMin, node.val), max(rightMax, node.val), currentSum
            
            return False, 0, 0, 0
        
        dfs(root)
        return self.maxSum

        