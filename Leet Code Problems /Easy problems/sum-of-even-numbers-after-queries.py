class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_sum = sum(filter(lambda x: x % 2 == 0, nums))

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            res.append(even_sum)

        return res
