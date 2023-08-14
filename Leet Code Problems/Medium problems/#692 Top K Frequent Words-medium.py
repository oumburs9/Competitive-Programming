class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

    
        freq = Counter(words)
        heap = []

        def insert(word):
            return (-freq[word], word)

        for word in freq:
            heapq.heappush(heap, insert(word))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result






  