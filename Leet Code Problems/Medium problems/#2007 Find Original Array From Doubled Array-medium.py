from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        l = len(changed)
        if l % 2 :
            return []
        count = Counter(changed)
        changed.sort()
        for item in changed:
            if item == 0 and count[item]>=2:
                count[item] -=2
                ans.append(item)
            elif item > 0 and count[item] and count[item*2]:
                count[item] -=1
                count[item*2] -=1
                ans.append(item)
             
        if len(ans)==l//2: 
            return ans
        return []