class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        numChild = 0
        cookieIndex = 0
        while cookieIndex < len(s) and numChild < len(g):
            if s[cookieIndex] >= g[numChild]:
                numChild += 1
            cookieIndex += 1
        return numChild


            

        