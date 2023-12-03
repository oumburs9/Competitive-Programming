class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        _list = s.split()
        length = max(len(s) for s in _list)
        res =['' for _ in range(length)]

        
        for i in range(len(_list)):
            for j in range(length):
                if j >= len(_list[i]):
                    if res[j]:
                        res[j] += ' '
                    else:
                        
                        res[j] = " " + res[j]
                 
                else:
                    res[j] += _list[i][j]
                    
                
                    
              
        
        return [re.rstrip() for re in res]
                           
            
            
        
        
        
        