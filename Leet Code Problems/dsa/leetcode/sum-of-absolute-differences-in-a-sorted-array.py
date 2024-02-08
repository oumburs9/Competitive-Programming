class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n


        prefixSum = []
        acc = 0
        for i in range(n):
            acc += nums[i]
            prefixSum.append(acc)

        suffixSum = [0]*n
        acc = 0
        for i in range(n-1,-1,-1):
            acc += nums[i]
            
            suffixSum[i] = acc
            

        for i in range(n):
            left = (nums[i] * i) - prefixSum[i]
            right = suffixSum[i] - (nums[i] * (n-i-1))
            
            res[i] =  left + right

        return res
        



        