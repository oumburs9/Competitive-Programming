class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j, result = 0, 0, []

        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])

            if start <= end:
                result.append([start, end])

            if A[i][1] < B[j][1]:
                i += 1
            elif A[i][1] >= B[j][1]:
                j += 1

        return result
        