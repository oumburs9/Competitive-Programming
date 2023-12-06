class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        res = []
        neg = []
        pos = []

        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        
        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(neg[i])
        return res
        