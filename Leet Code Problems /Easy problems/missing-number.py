class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1 = set(nums)

        for s in range(len(nums) + 1):
            if s not in set1:
                return s
        