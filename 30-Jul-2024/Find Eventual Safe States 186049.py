# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        num_nodes = len(graph)

        rev_graph, node_indeg = self.createReverseGraphAndIndegree(graph, num_nodes)

        safe_nodes = self.bfsFindSafeNodes(rev_graph, node_indeg, num_nodes)
        
        return safe_nodes

    def createReverseGraphAndIndegree(self, graph: List[List[int]], num_nodes: int):
    
        node_indeg = [0] * num_nodes

        rev_graph = [ [] for _ in range(num_nodes)]


        for node in range(num_nodes ):
            for nbr in graph[node]:

                rev_graph[nbr].append(node)  
                node_indeg[node] += 1             

        return rev_graph, node_indeg

    def bfsFindSafeNodes(self, rev_graph: List[List[int]], node_indeg: List[int], num_nodes: int) -> List[int]:
        queue = deque()
        
        for node in range(num_nodes):
           
            if node_indeg[node]== 0:
                queue.append(node)


        is_Safe_node= [False ] *num_nodes

        #  BFS 
        while queue:
            cur_node = queue.popleft()

            is_Safe_node[cur_node] = True

            
            for nbr in rev_graph[cur_node]:
                node_indeg[nbr] -= 1
                if node_indeg[nbr] == 0:
                    queue.append(nbr)

        # col safe
        return [node for node in range(num_nodes) if is_Safe_node[node] ]
