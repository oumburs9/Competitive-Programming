from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        counts_list = sorted(counts.items(), key=lambda x: x[1], reverse = True)

        output = []
        for char in counts_list:
            output.append(char[0] * char[1])

        return "".join(output)