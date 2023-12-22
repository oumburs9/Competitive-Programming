class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        scores = [0] * (len(nums) + 1)
        scores[0] = max_score = sum(nums)
        
        for i, num in enumerate(nums, 1):
            scores[i] = scores[i - 1] + (1 if num == 0 else -1)
            max_score = max(max_score, scores[i])
        
        return [index for index, score in enumerate(scores) if score == max_score]




        