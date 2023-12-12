class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        _setOfCard = set(fronts + backs)

        for fr, ba in zip(fronts,backs):
            if fr == ba:
                _setOfCard.discard(fr)
        

        return min(_setOfCard, default = 0)






        