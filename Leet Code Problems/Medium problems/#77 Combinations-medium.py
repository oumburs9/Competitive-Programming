class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
   
        nums = [num for num in range(1, n+1)]
        combinations = []

        def backtrack(i, combination):
            if len(combination) == k:
                combinations.append(combination[:])  # copying
                return
            if i >= n:
                return
            
            # inserting the number nums[i] into the combination and exploring the next index.
            combination.append(nums[i])
            backtrack(i+1, combination)
            combination.pop()  # Backtracking by removing the last inserted number.

            # do not insert the number nums[i] and explore the next index.
            backtrack(i+1, combination) 

        backtrack(0, [])  # start the backtracking process with i=0 and an empty combination.
        return combinations