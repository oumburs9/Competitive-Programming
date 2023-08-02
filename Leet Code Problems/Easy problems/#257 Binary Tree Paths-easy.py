# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, current_path):
            if not node:
                return []

            # append the current node value to the current path
            current_path.append(str(node.val))

            # If the node is a leaf (no children), return the path as a single-element list
            if not node.left and not node.right:
                return ["->".join(current_path)]

            # Recursively explore the left and right subtrees
            left_paths = dfs(node.left, current_path.copy())
            right_paths = dfs(node.right, current_path.copy())

            # Combine the paths from left and right subtrees and return the result
            return left_paths + right_paths

        # Start the DFS with the root node and an empty initial path
        return dfs(root, []) if root else []
