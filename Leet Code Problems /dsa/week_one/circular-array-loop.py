class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def helper(index):
            return (nums[index]+index)%len(nums)

        for i in range(len(nums)):
            if nums[i]==0: #to not to explore an already-explored node again
                continue
            slow, fast= i, helper(i)
            while True:
                if nums[slow]*nums[fast]>0 and nums[helper(fast)]*nums[fast]>0:
                    slow, fast = helper(slow), helper(helper(fast))
                    if fast==slow:
                        if fast!=helper(fast):
                            return True
                        break
                else:
                    break
            # if we end up here, we know either 
            # 1) the lenght of the cycle was 1: fast==helper(fast)
            # 2) we ran into an opposite jump: nums[helper(slow)]*nums[slow]
            # so we want to mark the nodes up to the point we see the opposite jump as already visited
            slow = i
            while nums[slow]!=0 and nums[helper(slow)]*nums[slow]>0:
                nums[slow], slow = 0, helper(slow)
        return False
        