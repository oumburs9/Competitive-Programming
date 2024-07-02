# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        adjecency_list = defaultdict(list)
        _set = set()

        for a, b in edges:
            adjecency_list[a].append(b)
            _set.add(a)
            _set.add(b)
        
        for k, v in adjecency_list.items():
            for b in v:
                if b in _set:
                    _set.remove(b)
        # print(_set)

        return list(_set)
        