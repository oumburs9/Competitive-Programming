
def maxFrequency( nums,k):
    nums.sort()
    
    left = 0
    right = 0
    tot = 0
    ans = 0
    
    while right < len(nums):
        tot += nums[right]  
        
        while nums[right]*(right-left+1) > tot + k:
            tot -= nums[left]
            left += 1
        ans = max(ans,right-left + 1)
        right +=1
    return ans

res = maxFrequency([1,2,4],5)
print(res)
    
    