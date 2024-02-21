class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1] 

        arrPrev = self.getRow(rowIndex-1)
        
        # start ...
        arr = [1]
        #  mid ...
        for i in range(1, len(arrPrev)):
            arr.append(arrPrev[i-1] + arrPrev[i])

        # end 1
        arr.append(1)
        return arr