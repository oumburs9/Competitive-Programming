class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        sorted_nums = sorted(nums)

        for i , num in enumerate(sorted_nums):
            if num not in count:
                count[num] = i
        return [count[num] for num in nums]
        