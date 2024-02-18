class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(lambda: 0)
        for a in answers:
            freq[a] += 1
        
        ans = 0
        for rabbit_said, numof in freq.items():
            ans += math.ceil(numof/(rabbit_said+1))*(rabbit_said+1)
        return ans
            
            
        