# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)  
    def helper(self, curNode, pathSum):
        if not curNode:  
            return 0

        pathSum = 10 * pathSum + curNode.val

        if not curNode.left and not curNode.right:
            return pathSum

        return (
            self.helper(curNode.left, pathSum) +
            self.helper(curNode.right, pathSum)
        )

# Example usage:
# Create a binary tree and call the sumNumbers function on its root
# solution = Solution()
# result = solution.sumNumbers(root)
# print(result)