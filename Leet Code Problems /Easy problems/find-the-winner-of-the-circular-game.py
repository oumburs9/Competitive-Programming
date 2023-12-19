class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i  for i in range(1,n+1)]
        
        i = 0
        while 1 < len(arr):
            i = (i + k -1) % len(arr)
            arr.pop(i)
        return arr[0]
           

            





        