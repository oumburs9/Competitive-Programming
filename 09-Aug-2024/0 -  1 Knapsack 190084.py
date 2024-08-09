# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def __init__(self):
        self.ans = 0
        self.memo = {}
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        def b_t(i, cur_val,cur_w):
            if cur_w > W:
                return float('inf')
                
            if i >= n:
                return cur_val
                # self.ans = max(self.ans, cur_val)
            state = (i, cur_val, cur_w)
            if state in self.memo:
                return self.memo[state]
                
                
            self.memo[state] = max( b_t(i+1, cur_val + val[i], cur_w + wt[i]), b_t(i+1, cur_val, cur_w))
            
            return self.memo[state]
            
            
            
        b_t(0, 0, 0)
        
        return self.ans
        