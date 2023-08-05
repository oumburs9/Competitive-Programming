# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root is None):
            return 0
        if(root.left is None and  root.right is None):
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right)+1

#  another approach  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # (1) recursive
        # def find_max(node):
        #     if not node: return 0
        #     left = 1 + find_max(node.left)
        #     right = 1 + find_max(node.right)

        #     return max(left,right)
        # return find_max(root)

        #(2) iterative
        if not root: return 0

        stack = [(root,1)]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append((node.left,depth + 1))
                stack.append((node.right,depth + 1))
        return res


