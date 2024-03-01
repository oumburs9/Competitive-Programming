class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        def backtrack(oc, cc, curr):
            
            if len(curr) == 2*n:
                res.append(''.join(curr))
                return
                
            if oc < n:
                curr.append('(')
                backtrack(oc + 1, cc, curr)
                curr.pop()
                
            if cc < oc:
                curr.append(')')
                backtrack(oc, cc + 1, curr)
                curr.pop()
                
        res = []
        backtrack(0,0,[])   
        
        return res
        
                            
            