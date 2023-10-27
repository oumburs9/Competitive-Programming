class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_consecutive = 0
        left = 0
        max_count = 0  # Maximum count of 'T's or 'F's in the window
        counts = {'T': 0, 'F': 0}

        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1
            max_count = max(max_count, counts['T'], counts['F'])

            # Check if the window can be expanded
            while (right - left + 1 - max_count) > k:
                counts[answerKey[left]] -= 1
                left += 1

            max_consecutive = max(max_consecutive, right - left + 1)

        return max_consecutive
