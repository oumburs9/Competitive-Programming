class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboardList = ['qwertyuiop','asdfghjkl' ,'zxcvbnm']
        res = []
        for word in words:
            word_lower = word.lower()
            row = None
            for idx , val in enumerate(keyboardList):
                if word_lower[0] in val:
                    row = idx
                    break
            if row is not None and all(c in keyboardList[row]  for c in word_lower):
                res.append(word)
        return res




        
                


        