# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        current =[]
        

        def backtrack(index):
            
            if index >= len(s): 
                return len(current) >= 2
            
            for i in range(index,len(s)):
                val = int(s[index:i+1])
                if len(current) == 0 or val == current[-1] -1:
                    current.append(val)
                    if backtrack(i+1):
                        return True
                    current.pop()
            return False

        return backtrack(0)
        