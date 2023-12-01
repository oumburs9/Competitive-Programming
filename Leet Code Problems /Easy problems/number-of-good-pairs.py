class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        goodPair =0
        count = Counter(nums)
        
        for i in range(len(nums)):
            if nums[i-1] == nums[i] and i != 0:
                continue
            n = count[nums[i]]
            print(nums[i],n)
            goodPair += n*(n-1)//2
        return goodPair
        