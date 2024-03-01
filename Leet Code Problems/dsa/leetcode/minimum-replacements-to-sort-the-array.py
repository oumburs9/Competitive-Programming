# class Solution:
#     def minimumReplacement(self, nums: List[int]) -> int:
#         n = len(nums) - 1
#         count = 0
#         for i in range(n - 1,-1,-1):
#             while nums[i] > nums[i + 1]:
#                 diff = nums[i] - nums[i+1]
#                 if diff <= ceil(nums[i+1]/2):
#                     nums[i] = nums[i]//2
#                     count += 1
#                     continue

#                 nums[i] = diff
#                 count += 1

#         return count
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0

        prev = nums[n - 1]

        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                k = math.ceil(nums[i] / prev)
                ops += k - 1
                prev = nums[i] // k
            else:
                prev = nums[i]
        return ops