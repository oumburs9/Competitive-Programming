class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexDict = {}

        for i in range(len(s)):
            indexDict[s[i]] = i

        start, end = 0, 0
        res = []

        for i in range(len(s)):
            end = max(end,indexDict[s[i]])
            if end == i:
                res.append(end - start + 1 )
                start = i+1
        return res
            





        