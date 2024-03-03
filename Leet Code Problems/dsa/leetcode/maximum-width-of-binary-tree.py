# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        q = deque([(root, 0) ])

        _maxWidth = 0
        
        while q:
            _length = len(q)
            minIdx = q[0][1]

            f_idx, l_idx = 0, 0
            
            for j in range(_length):
                currNode, currIdx = q.popleft()
                currIdx -= minIdx
                
                if j == 0:
                    f_idx = currIdx
                
                if j == _length - 1:
                    l_idx = currIdx
                
                if currNode.left:
                    q.append((currNode.left, 2 * currIdx + 1))
                
                if currNode.right:
                    q.append((currNode.right, 2 * currIdx + 2))
            
            _maxWidth = max(_maxWidth, l_idx - f_idx + 1)
        
        return _maxWidth