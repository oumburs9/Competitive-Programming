class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()  

        def backtrack(cur, idx):
            res.append(cur[:]) 
            for i in range(idx, len(nums)):
                # skip here..\
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])

                backtrack(cur, i + 1)

                cur.pop()

        backtrack([], 0)

        return res
