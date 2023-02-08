
from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i]= 1 if (nums[i]%2 != 0) else  0
            
        prefixSum , count = 0,0
        dic = defaultdict(int)
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            
            if prefixSum ==k:
                count +=1
            if prefixSum-k in dic:
                count += dic[prefixSum-k]
            dic[prefixSum] = dic.get(nums[i], 0) + 1
        return count
                    
         
  
        