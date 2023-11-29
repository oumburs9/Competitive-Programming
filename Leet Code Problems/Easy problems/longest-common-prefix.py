class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def two2(a,b):
            com = ''
            for i in range(min(len(a),len(b))):
                if a[i] != b[i]:
                    return com
                com += a[i]
            return com
        
        ans  = strs[0]
        for i in range(1,len(strs)):
            ans = two2(ans,strs[i])
        return ans
            

        