class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 
        prefixSumFreq = defaultdict(int)
        prefixSumFreq[0] = 1
        prefixSum = 0 

        for num in nums:
            prefixSum += num
            rem = prefixSum % k

            if rem < 0:
                rem += k

            count += prefixSumFreq[rem]
            prefixSumFreq[rem] += 1

        return count  
























