class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 
        prefixSum = {0: 1}  # Dictionary to store prefix sums and their frequencies
        currentSum = 0 

        for num in nums:
            currentSum += num 
            rem = currentSum % k  # the remainder

            if rem < 0:
                rem += k  # If rem is negative, add k to make it positive

            if rem in prefixSum:
                count += prefixSum[rem]  # Add the frequency of rem to count

            prefixSum[rem] = prefixSum.get(rem, 0) + 1  # Increment the frequency of rem in prefixSum

        return count  
