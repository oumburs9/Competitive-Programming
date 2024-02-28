# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = deque()
        queue.append(root)
        switch = False

        while queue:
            level_size = len(queue) # len
            level_vals = deque()
            for _ in range(level_size):
                node = queue.popleft()
                if not switch:
                    level_vals.append(node.val)
                else:
                    level_vals.appendleft(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            switch = not switch
            result.append(level_vals)
        return result


