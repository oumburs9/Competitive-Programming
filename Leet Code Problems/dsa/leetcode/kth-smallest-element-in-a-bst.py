# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
        # If k becomes zero, we have found the kth smallest element.
        if self.k == 0:
            self.res = root.val
            return
            
        self.helper(root.right)
