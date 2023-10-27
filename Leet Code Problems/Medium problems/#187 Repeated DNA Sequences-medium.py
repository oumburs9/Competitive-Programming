class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        sequences = defaultdict(int)
        result = []
        
        # init the sliding window and process the first 10-letter sequence
        window = s[:10]
        sequences[window] = 1

        for i in range(10, len(s)):
            # slide the wind
            window = window[1:] + s[i]

            # count
            sequences[window] += 1

            # add it to the result
            # if the current window sequence occurs twice,
            if sequences[window] == 2:
                result.append(window)

        return result
