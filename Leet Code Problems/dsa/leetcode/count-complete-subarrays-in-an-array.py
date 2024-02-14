class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        length = len(set(nums))
        freqDict = {}
        left ,res = 0, 0

        for r in range(n):
            freqDict[nums[r]] = freqDict.get(nums[r], 0) + 1

            while len(freqDict) == length:
                res += n - r
                freqDict[nums[left]] -= 1
                if freqDict[nums[left]] == 0:
                    del freqDict[nums[left]]
                left += 1

        return res
        