class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        indexDict = defaultdict(int)
        res = float('-inf')
        prefixSum = [0]
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            prefixSum.append(acc)

        startWind = 0
        
        for endWind in range(len(nums)):
            if nums[endWind] in indexDict:
                startWind = indexDict[nums[startWind]] + 1
           
            res = max(res, prefixSum[endWind + 1] - prefixSum[startWind])


            indexDict[nums[endWind]] = endWind
        return res

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        indexDict = {nums[0]: 0}
        maxSum = nums[0]
        l = -1
        
        for r in range(1, len(nums)):
            if nums[r] in indexDict:
                l = max(l, indexDict[nums[r]])
            
            indexDict[nums[r]] = r
            
            nums[r] += nums[r-1]


			
            curSum = nums[r] - nums[l] if l != -1 else nums[r]
            maxSum = max(maxSum,  curSum)
                
        return maxSum
        
        




        