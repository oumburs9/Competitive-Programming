# def majorityEl(nums):
#     m = {}
#     for i in range(len(nums)):
#         if(nums[i] in m):
#             m[nums[i]] +=1
#         else:
#             m[nums[i]] = 1
#     return max(m.keys())



def majorityElement(nums):
    m = {}
    print(nums)
    for num in nums:
        m[num] = m.get(num,0)+1
        print(m)
    for num in nums:
        if(m[num]>len(nums)//2):
            return num


res = majorityElement([2,2,2,3,3,2])
print(res)


