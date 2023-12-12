class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = [i for i in s.split(" ") if i != '']
        left, right = 0 , len(s)-1
        print(s)

        while left < right:
            s[left] , s[right] =  s[right] , s[left]
            left += 1
            right -= 1
            
        return " ".join(s)
            
        