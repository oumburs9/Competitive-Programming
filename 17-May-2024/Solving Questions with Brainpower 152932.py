# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        dp = [0]*n
        for i in range(n - 1, -1, -1):
            dp[i] = questions[i][0]

            valid_index = i + questions[i][1] + 1
            if valid_index < n:
                dp[i] += dp[valid_index]

            if i + 1 < n:
                dp[i] = max(dp[i], dp[i + 1])
        return dp[0]