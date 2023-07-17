class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        res = [0] * (n + 1)  # Initialize a list to store cumulative shifts at each position
        
        # Calculate the cumulative shifts for each position
        for start, end, direction in shifts:
            if direction == 1:  # (If the direction is 1, add 1 to the shifts in the range)
                res[start] += 1
                res[end + 1] -= 1
            else:  # ( If the direction is 0, subtract 1 from the shifts in the range )
                res[start] -= 1
                res[end + 1] += 1
        
        # Calculate the cumulative sum of the shifts
        for i in range(1, n):
            res[i] += res[i - 1]
        
        # Build the resulting string by applying the shifts to each character
        result = ""
        for i, c in enumerate(s):
            shift = (ord(c) - 97 + res[i]) % 26  # ( Calculate the new position of the character )
            shifted_char = chr(shift + 97)  # ( Convert the new position to the corresponding lowercase character )
            result += shifted_char  # ( Add the shifted character to the result string )
        
        return result 

