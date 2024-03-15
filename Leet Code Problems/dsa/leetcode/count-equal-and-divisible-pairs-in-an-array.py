class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        d = defaultdict(list)
        n = len(nums)
        for i in range(n):
            if nums[i] in d:
                for ind in d[nums[i]]:
                    if (ind *i ) % k == 0:
                        res += 1
            d[nums[i]].append(i)
        return res
        