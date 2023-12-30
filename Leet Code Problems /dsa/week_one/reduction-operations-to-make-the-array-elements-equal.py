class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        unique_nums = sorted(set(nums))
        freq = {num: index for index, num in enumerate(unique_nums)}
        ans = sum(freq[num] for num in nums)

        return ans


        