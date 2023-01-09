def rearrangeArray(nums):
    for i in range(1,len(nums)-1):
        print( (nums[i-1] + nums[i+1]) / 2,nums[i])

        if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
            # print(nums)
            # print(nums.pop(nums[i]))
            print(nums)
            # nums.append(nums.pop(nums[i]))
            nums[i],nums[i+1] =nums[i+1],nums[i]
    print(nums)
    return nums


res = rearrangeArray([1,2,3])
print(res)
        