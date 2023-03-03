from typing import List

#approach 1 using map
def dublicateNum(nums):
    m = {}
    for i in range(len(nums)):
        if(nums[i] in m):
            return True
        m[i] = nums[i]
    return False

res =dublicateNum([1,2,3,1])
print(res)

# approach 2 using sets
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        window = set()
        
        for e in range(len(nums)):
            if nums[e] in window:
                return True
            window.add(nums[e])
        return False