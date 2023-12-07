class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            _curS = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    _curS += abs(i-j)
            res.append(_curS)

        return res

