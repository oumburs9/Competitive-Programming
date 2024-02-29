# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)  # Start the computation by calling the helper function

    def helper(self, curNode, pathSum):
        if not curNode:  # If the current node is None, return 0
            return 0

        # Update pathSum by shifting digits and adding the current node's value
        pathSum = 10 * pathSum + curNode.val

        # If the current node is a leaf node (no left or right child), return pathSum
        if not curNode.left and not curNode.right:
            return pathSum

        # Recursively calculate the sum of numbers from left and right subtrees
        return (
            self.helper(curNode.left, pathSum) +
            self.helper(curNode.right, pathSum)
        )

# Example usage:
# Create a binary tree and call the sumNumbers function on its root
# solution = Solution()
# result = solution.sumNumbers(root)
# print(result)
