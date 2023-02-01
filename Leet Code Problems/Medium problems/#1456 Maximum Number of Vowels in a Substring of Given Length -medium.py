
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
       
        vowels = 'aeiou'
        max_count = 0
        indx = 0
        
        
        for v in range(k):
            if s[v] in vowels :
                max_count+=1
        
        curr_count = max_count

        for i in range(k,len(s)):
            
                if s[indx] in vowels:
                    curr_count-=1
                    
                if s[i] in vowels:
                    curr_count+=1

                indx+=1

                max_count=max(max_count,curr_count)
        
        return max_count
        