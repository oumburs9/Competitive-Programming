# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        que = deque()
        que.append(root)

        while que:
            n = len(que)
            curr_sum = 0
            for _ in range(n):
                node = que.popleft()
                curr_sum += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            res.append(curr_sum / n)

        return res
        