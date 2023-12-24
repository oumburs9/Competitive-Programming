class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        i = 0
        m = len(strs)
        n = len(strs[0])
        count = 0
        while (i < n):
            for j in range(m-1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1
                    break
            i += 1
        return count
            