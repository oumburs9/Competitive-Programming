def dublicateNum(nums):
    m = {}
    for i in range(len(nums)):
        if(nums[i] in m):
            return True
        m[i] = nums[i]
    return False

res =dublicateNum([1,2,3,1])
print(res)