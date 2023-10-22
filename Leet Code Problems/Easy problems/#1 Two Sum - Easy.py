class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            # finding goal
            complement = target - nums[i]
            
            # checking the if the goal was already in d
            if complement in dic:
                return [dic[complement],i]
            # keeping the current val in dictionary 
            dic[nums[i]] = i
        return []
     



        

def twoSum2(nums,target):
    m = {}
    for i in range(len(nums)-1):
        goal = target - nums[i]
        if goal in m:
            return [m[goal],i]
        m[nums[i]] = i

res = twoSum2([2,7,11,15],9)
print(res)