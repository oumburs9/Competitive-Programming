from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        windowSet = set()
        
        startWindow = 0
        
        for endWindow in range(len(nums)):
            if nums[endWindow] in windowSet and  endWindow - startWindow <= k :
                return True
                
            windowSet.add(nums[endWindow])
            
            if endWindow - startWindow >= k:
                
                windowSet.remove(nums[startWindow])
                startWindow +=1
                
        return False
                
                
                
            
            
        