# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        degree = [0]*n
        adjecency_list = defaultdict(set)

        # calc the degree
        for a, b in roads:
            adjecency_list[a].add(b)
            adjecency_list[b].add(a)

            degree[a] += 1
            degree[b] += 1

        # calc the max network rank
        res_max_rank= 0 
        for i in range(n):
            for j in range(i+1,n):
                curr_rank = degree[i] + degree[j]

                if j in adjecency_list[i]:
                    curr_rank -= 1
                    
                res_max_rank = max(res_max_rank, curr_rank)
        return res_max_rank
                


        