class Solution:

    def backtracking(self, ans, m, digits, combination, index):
        if (index > len(digits)):
            return
        if (len(combination) == len(digits)):
            ans.append(combination[:])
            return

        currentDigit = digits[index]
        curString = m[currentDigit]

        for i in range(len(curString)):
            self.backtracking(ans, m, digits, combination +
                              curString[i], index+1)

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if (len(digits) == 0):
            return ans

        m = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        self.backtracking(ans, m, digits, "", 0)

        return ans
