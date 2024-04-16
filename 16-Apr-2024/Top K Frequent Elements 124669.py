# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _s = list(set(nums))
        
        _min = min(nums)
        count = [0]*(max(nums)- _min + 1)

        for num in nums:
            count[num - _min] += 1

        _s.sort(key = lambda x: count[x - _min], reverse=True)

        return _s[:k]
            





        







        