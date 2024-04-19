# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cntr = Counter(deck)

        gcdval = cntr[deck[0]]
        for cnt in cntr.values():
            gcdval = gcd(gcdval, cnt)
        return gcdval > 1
        