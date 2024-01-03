class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_con = ''
        for alnum in s.lower():
            if alnum.isalnum():
                word_con += alnum
        
        left, right = 0, len(word_con)-1

        while left < right:
            if word_con[left] != word_con[right]:
                return False
            left += 1
            right -= 1
        return True

        