class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(combination, index):
            nonlocal digits, m, res
            if index > len(digits):
                return
            if len(combination) == len(digits):
                res.append(combination[:])
                return

            currentDigit = digits[index]
            curString = m[currentDigit]

            for i in range(len(curString)):
                backtracking( combination + curString[i], index + 1)

        res = []
        if len(digits) == 0:
            return res

        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        backtracking("", 0)

        return res
