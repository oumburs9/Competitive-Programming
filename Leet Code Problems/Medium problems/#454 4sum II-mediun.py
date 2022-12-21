def fourSum(a,b,c,d):
    ans = 0
    m = {}

    for i in a:
        for j in b:
            k = i+j
            if k not in m:
                m[k]= 0
            m[k] +=1
    for i in c:
        for j in d:
            k = -(i+j)
            if k in m:
                ans += m[k]
    return ans

nums1 = [1,2]
nums2 = [-2,-1] 
nums3 = [-1,2]
nums4 = [0,2]
res = fourSum(nums1,nums2,nums3,nums4)
print(res)