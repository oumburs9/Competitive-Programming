class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        max_res = 0
        count = 0
        el = 0
        
        for i in range(len(arr)):
            if  i > 0 and arr[i] != arr[i - 1]:
                count = 1
                continue
            count += 1
            if max_res < count:
                max_res = count
                el = arr[i]

        return el



            