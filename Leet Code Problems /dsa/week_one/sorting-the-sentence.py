class Solution:
    def sortSentence(self, s: str) -> str:

        _list = s.split()

        _list.sort(key= lambda x: x[-1])


        return ' '.join(el[:len(el)-1] for el in _list )

        