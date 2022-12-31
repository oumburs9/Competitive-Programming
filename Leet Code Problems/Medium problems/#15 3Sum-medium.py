
# def threeSum(nums):
#     ans = []
#     for i in range(len(nums)-1):
#         first = i+1
#         last = first + 1
#         while (last < len(nums)):
#             curAns = []
#             car = nums[i] + nums[first] + nums[last]
#             if car == 0:
#                 curAns.append(nums[i])
#                 curAns.append(nums[first])
#                 curAns.append(nums[last])
#                 ans.append(curAns)
#             first += 1
#             last = first + 1 

#     return ans



# nums = [-1, 0, 1, 2, -1, -4]
# res = threeSum(nums)
# print(res)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

