# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)

        masks = [0] * n
        lengths = [0] * n
        
        for i in range(n):
            bitmask = 0

            for c in words[i]:
                bitmask |= 1 << ( ord(c) - ord('a') )


            masks[i] = bitmask
            lengths[i] = len(words[i])
        
        max_pr = 0
        
        # cmp each pair of words
        for i in range(n):
            for j in range(i + 1, n):
                    # No common
                if masks[i] & masks[j] == 0:  
                    max_pr = max(max_pr, lengths[i] * lengths[j])
        
        return max_pr
