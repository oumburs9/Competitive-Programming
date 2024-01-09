class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        startWindow, ans = 0,0    # initialize k to be one, meaning we could have at most one zero in the sliding window
        for endWindow in range(len(nums)):
            if nums[endWindow] == 0:
                k -= 1
            while k < 0:
                if nums[startWindow] == 0:
                    k+=1
                startWindow +=1
            ans = max(ans,endWindow - startWindow +1 )
        return ans

        