
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        
        group_a, group_b = set(), set()

        def is_bi(u: int, ga: set[int], gb: set[int]) -> bool:
          
            return u not in gb and (ga.add(u) or all(is_bi(v, gb, ga) for v in graph[u] if v not in gb))

       
        for u in range(len(graph)):
          
            if u not in group_a and u not in group_b:
                if not is_bi(u, group_a, group_b):
                    return False  

        return True  



        