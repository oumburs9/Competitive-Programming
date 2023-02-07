from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans , windowSum, startWindow ,target = 0, 0, 0 , threshold*k
        
        for endWindow in range(len(arr)):
            windowSum += arr[endWindow]
            
            if endWindow > k-1:
                windowSum -= arr[startWindow]
                startWindow +=1
                
            if windowSum >= target and endWindow >= k -1:
                ans +=1
                
        return ans
                
        