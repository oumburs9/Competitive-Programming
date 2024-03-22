class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        res = []

        for i in range(len(nums)):
            freq[nums[i]] += 1

            if freq[nums[i]] == 2:
                res.append(nums[i])
        return res

        