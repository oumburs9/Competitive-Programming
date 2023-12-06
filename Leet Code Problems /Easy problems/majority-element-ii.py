class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        counter = Counter(nums)
        for i,c in counter.items():
            if c > len(nums) // 3:
                res.append(i)
        return res
        