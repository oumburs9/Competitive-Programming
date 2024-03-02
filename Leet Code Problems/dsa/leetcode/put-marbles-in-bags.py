class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        pairWeights = []
        for i in range(n - 1):
            pairWeights.append(weights[i] + weights[i + 1])

        pairWeights.sort()  
        
        if k == 1:
            return 0
        
        maxSum = sum(pairWeights[-(k - 1):])
        minSum = sum(pairWeights[:k - 1])
        
        return maxSum - minSum
