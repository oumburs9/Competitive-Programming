class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) in used:
                    continue  
                    
                if i in used:
                    continue 

                perm.append(nums[i])

                used.add(i)

                backtrack(perm)

                perm.pop()
                used.remove(i)
        
        res = []
        nums.sort()
        used = set()
        backtrack([])
        return res




