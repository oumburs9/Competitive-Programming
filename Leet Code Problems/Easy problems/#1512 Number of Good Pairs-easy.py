from collections import Counter


def numIdenticalPairs(nums) -> int:
        nums.sort()
        goodPair =0
        count = Counter(nums)
        
        for i in range(len(nums)):
            if nums[i-1] == nums[i] and i!=0:
                continue
            n = count[nums[i]]
            print(nums[i],n)
            goodPair += n*(n-1)//2
        return goodPair
# res = numIdenticalPairs([1,2,3,1,1,3])
res = numIdenticalPairs([1,1,1,1])
print(res)