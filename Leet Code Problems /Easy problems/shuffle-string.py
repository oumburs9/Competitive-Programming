class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0]*len(indices)
        for si , i in zip(s,indices):
            res[i] = si
        return ''.join(res)
