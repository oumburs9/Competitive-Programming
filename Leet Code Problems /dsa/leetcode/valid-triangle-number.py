class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(2,len(nums)):
            start = 0
            end = i-1
            ans = 0
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    ans += end - start
                    end -= 1
                else:
                    start += 1
            count += ans
        return count




        