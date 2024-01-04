class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        count = 0
        nums.sort()
        left, right = 0, len(nums)-1

        while left < right:
            # [-1,1,1,2,3,]
            if nums[left] + nums[right] < target:
                count += right - left  # All pairs with nums[left] will satisfy the condition
                left += 1
            else:
                right -= 1

        return count


        