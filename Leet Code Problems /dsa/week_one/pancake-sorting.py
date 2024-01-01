class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []  

        for i in range(len(arr) - 1, 0, -1):
            maxIndex = arr.index(i + 1)  
            if maxIndex != i:
                arr[:maxIndex + 1] = arr[:maxIndex + 1][::-1]
                flips.append(maxIndex + 1)  
                arr[:i + 1] = arr[:i + 1][::-1]
                flips.append(i + 1)  

        return flips  










        
        
        