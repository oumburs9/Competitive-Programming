class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indexDict = defaultdict(int)
        _min = float('inf')

        for i in range(len(cards)):
            if cards[i] in indexDict:
                _min = min(_min,i- indexDict[cards[i]] + 1 )
            indexDict[cards[i]] = i
        return -1 if _min == float('inf') else _min

        