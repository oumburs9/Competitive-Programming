class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        curr = 0
        
        for i in range(-k,k):
            curr +=cardPoints[i]
            
            if i >= 0:
                curr -= cardPoints[i-k]
                
            ans = max(curr,ans)
        return ans
                
            
        