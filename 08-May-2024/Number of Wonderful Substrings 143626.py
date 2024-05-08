# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1023 
        mask = 0
        total = 0

        for char in word:
            idx = ord(char) - ord('a')
            mask ^= 1 << idx  
            total += count[mask]

            for i in range(10):
                total += count[mask ^ (1 << i)]
            
            count[mask] += 1

        return total