# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)

        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.helper(root.right)


# ********************** DESCRIPTIONS*************************

#         # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         # Initialize the class variables to track k and the result.
#         self.k = k
#         self.res = None

#         # Call the helper function to perform the kth smallest element search.
#         self.helper(root)

#         # Return the kth smallest element found.
#         return self.res

#     def helper(self, root):
#         # Base case: If the current node is None, return.
#         if not root:
#             return

#         # Traverse the left subtree recursively.
#         self.helper(root.left)

#         # Decrement k since we have visited a node.
#         self.k -= 1

#         # If k becomes zero, we have found the kth smallest element.
#         if self.k == 0:
#             self.res = root.val
#             return

#         # Traverse the right subtree recursively.
#         self.helper(root.right)

