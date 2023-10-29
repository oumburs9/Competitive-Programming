class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result = []

        for i in range(word_len):
            left, right, count = i, i, 0
            current_count = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    if word in current_count:
                        current_count[word] += 1
                    else:
                        current_count[word] = 1
                    count += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        left += word_len
                        current_count[left_word] -= 1
                        count -= 1

                    if count == len(words):
                        result.append(left)

                else:
                    current_count.clear()
                    count = 0
                    left = right

        return result
        