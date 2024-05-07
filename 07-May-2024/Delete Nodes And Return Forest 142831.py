# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        del_set = set(to_delete)
        forest = []
        def dfs(node, has_parent):
            if not node:
                return None

            should_delete = node.val in del_set
            if not should_delete and not has_parent:
                forest.append(node)

            # 
            node.left = dfs(node.left, not should_delete)
            node.right = dfs(node.right, not should_delete)

            return None if should_delete else node

        dfs(root, False)
        return forest