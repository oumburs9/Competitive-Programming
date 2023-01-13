class Solution:
    def sortSentence(self, s: str) -> str:
        aArr = s.split()
        aArr.sort(key=lambda x: int(x[-1]))
        return " ".join(x[:-1] for x in aArr)