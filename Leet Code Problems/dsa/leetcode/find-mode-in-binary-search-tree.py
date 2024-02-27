# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        _freqMode = defaultdict(int)
        def dfs(node):
            nonlocal _freqMode

            if not node:
                return 0

            _freqMode[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        _freq = max(_freqMode.values())

        return [ key for key,val in _freqMode.items() if val == _freq]
        