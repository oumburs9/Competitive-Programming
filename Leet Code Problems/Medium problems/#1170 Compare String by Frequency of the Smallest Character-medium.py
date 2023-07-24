from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        
        words_freq_sorted = sorted(map(f, words))
        n = len(words_freq_sorted)
        # 
        def binary_search(arr, target):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return n - left
        
        res = []
        for query in queries:
            query_freq = f(query)
            res.append(binary_search(words_freq_sorted, query_freq))
        
        return res
