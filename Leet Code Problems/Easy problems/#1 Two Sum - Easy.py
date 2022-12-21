def twoSum(nums,target):
    for i in range(len(nums)-1):
        if(nums[i]+nums[i+1]==target):
            return [i,i+1]

res = twoSum([2,7,11,15],9)
print(res)

def twoSum2(nums,target):
    m = {}
    for i in range(len(nums)-1):
        goal = target - nums[i]
        if goal in m:
            return [m[goal],i]
        m[nums[i]] = i

res = twoSum2([2,7,11,15],9)
print(res)