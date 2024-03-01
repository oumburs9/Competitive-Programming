class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        counter = Counter(window)
        res = counter['W']

        print(window,counter,res)

        for i in range(k,len(blocks)):
            counter[blocks[i]] += 1
            counter[window[0]] -= 1
            window = window[1:] + blocks[i]

            res = min(res,counter['W'])

        return res






        