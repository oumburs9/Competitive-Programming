class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i

        for i in range(len(words)-1):
            for j in range(min(len(words[i]),len(words[i+1]))):
                if dic[words[i][j]] < dic[words[i+1][j]]:
                    break
                elif dic[words[i][j]] == dic[words[i+1][j]]:
                    continue
                else:
                    return False
            else: 
                # Check for the case where one word is a prefix of another
                if len(words[i]) > len(words[i+1]):
                    return False

        return True

        


            
        