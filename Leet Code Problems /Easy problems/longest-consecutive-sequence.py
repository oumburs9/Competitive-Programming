class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in numsSet:
                curNum = num
                while curNum in numsSet:
                    curNum += 1
                longest = max(longest,curNum - num )

        return longest

            

        


        