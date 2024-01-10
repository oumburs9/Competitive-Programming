class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # freq
        counter = Counter(nums)

        index = 0
        for c in range(3):
            for _ in range(counter[c]):
                nums[index] = c
                index += 1
        return nums

        