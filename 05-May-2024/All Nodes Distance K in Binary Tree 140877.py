# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import deque
        from typing import List

        def dfs(node, par):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)

    
        parent = {}
        dfs(root, None)  #dfs st

        que = deque([(target, 0)])
        seen = set([target])

        res = []

        while que:
            cur, dist = que.popleft()

            if dist == k:
                res.append(cur.val)
            elif dist < k:

                for neighbor in (cur.left, cur.right, parent[cur]):
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)

                        que.append((neighbor, dist + 1))

        return res