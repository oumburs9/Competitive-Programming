# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        n = len(nums)
        for s in range(n):
            while True:
                c = nums[s] - 1
                if s == c or nums[s] == nums[c]:
                    break
                nums[s], nums[c] = nums[c], nums[s]

        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
        