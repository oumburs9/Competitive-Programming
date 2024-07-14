# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_degree = [0] * n
    
        for i in range(n):
            if leftChild[i] != -1:
                in_degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                in_degree[rightChild[i]] += 1
        
        root_count = in_degree.count(0)
        if root_count != 1:
            return False
        
        root = in_degree.index(0)
        
        visited = [False] * n
        stack = [root]
        visited_count = 0
        
        while stack:
            node = stack.pop()
            if visited[node]:
                return False
            visited[node] = True
            visited_count += 1
            if leftChild[node] != -1:
                stack.append(leftChild[node])
            if rightChild[node] != -1:
                stack.append(rightChild[node])
        
        return visited_count == n