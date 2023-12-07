class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
                                        
        set1 = { el for arr in ranges for el in range(arr[0],arr[1]+1) }

        for i in range(left,right +1):
            if i not in set1:
                return False
        return True

        