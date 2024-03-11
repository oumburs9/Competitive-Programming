class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
       
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return [-1,-1] if len(ans)==0 else [ans[0],ans[-1]]
        