class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        pDist = abs(target[0]) + abs(target[1])
        for g in ghosts:
            gDist = abs(g[0]- target[0]) + abs(g[1]-target[1])

            if gDist <= pDist:
                return False

        return True
        