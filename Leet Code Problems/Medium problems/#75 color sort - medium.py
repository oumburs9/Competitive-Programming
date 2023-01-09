def sortColors( nums):
    print(nums)
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if(nums[j-1]>=nums[j]):
                nums[j-1],nums[j] = nums[j],nums[j-1]
                print(nums)
        print(',,,,,,,,,,')
    return nums

res = sortColors([2,0,2,1,1,0])
print(res)