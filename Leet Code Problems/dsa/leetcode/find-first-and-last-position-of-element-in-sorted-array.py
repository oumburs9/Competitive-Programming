class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1

        # start
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2

            if nums[mid] == target:
                start = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        # end
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2

            if nums[mid] == target:
                end = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return [start, end]


