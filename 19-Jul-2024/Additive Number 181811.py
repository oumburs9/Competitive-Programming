# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        path = []  

        def backtrack(index, nums):  
            if index == len(nums) and len(path) >= 3:  
                return True

            for i in range(index, len(nums)):
                if nums[index] == "0" and i != index:
                    break
                n = int(nums[index:i + 1])

                if len(path) >= 2 and path[-2] + path[-1] < n:  
                    break

                if len(path) <= 1 or path[-2] + path[-1] == n: 
                    path.append(n)
                    if backtrack(i + 1, nums):  
                        return True
                    path.pop()

            return False

        return backtrack(0, num)