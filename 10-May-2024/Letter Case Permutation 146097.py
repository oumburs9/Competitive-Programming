# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letIdx = [i for i, c in enumerate(s) if  c.isalpha()       ]
        print(letIdx)
       
        n = len(letIdx)
        res = []

        for m in range(1 << n): #

            perm = list(s)

            for i, idx in enumerate(letIdx):
                ''' 
                print('m: ', m, 'i: ', i)
                print('1 << i: ', 1<<i)
                print('m & (1 << i): ', m & (1 << i))
                '''
                if m & (1 << i):
                    perm[idx] = perm[idx].upper()
                    
                else:
                    perm[idx] = perm[idx].lower()

            res.append("".join(perm))


        return res