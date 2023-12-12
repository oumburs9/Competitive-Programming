class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexDict:
                return [ indexDict[diff], i ]
            indexDict[nums[i]] = i
            


        