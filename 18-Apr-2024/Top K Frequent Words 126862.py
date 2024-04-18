# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = defaultdict(int)
        
        for word in words:
            freq[word] += 1

        top_k = sorted(freq.keys(), key= lambda x: (-freq[x], x))
        return top_k[:k]

    
 






  