def longestSubstringWithoutRep(s):
    l = r = ans = 0
    dict = {}
    length = len(s)

    while (l < length and r < length):
        curEl = s[r]

        if(curEl in dict):
            l = max(l,dict[curEl]+1)
        dict[curEl]=r
        ans = max(ans,r-l+1)
        r+=1
    return ans
    
s = 'jabiri'
res =longestSubstringWithoutRep(s=s)
print(res)