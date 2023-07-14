from ast import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        acc = 0
        
        for i in range(len(nums)):
            acc += nums[i]
            runningSum.append(acc)
        return runningSum


# from typing import List


# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         prefixSum = []
#         total = 0
        
#         for i in range(len(nums)):
#             total +=nums[i]
#             prefixSum.append(total)
#         return prefixSum
            