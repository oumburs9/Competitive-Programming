from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
       
        
        
        def sortAnsReturnBool(left,right):
            newList = list(sorted(nums[left:right+1]))
            
        
            if len(newList)==1:
                return True
            
            dif = newList[1] - newList[0]

            for i,j in zip(newList,newList[1:]):
                if dif != j - i:
                    return False
            return True
        
        ans = []
        for left,right in zip(l,r):
            ans+=[sortAnsReturnBool(left,right)]
        return ans