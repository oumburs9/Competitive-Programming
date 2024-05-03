# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        segments1 = version1.split('.')
        segments2 = version2.split('.')
        
        max_length = max(len(segments1), len(segments2))
        
        for i in range(max_length):
            int1 = int(segments1[i]) if i < len(segments1) else 0
            int2 = int(segments2[i]) if i < len(segments2) else 0
            
            if int1 < int2:
                return -1
            elif int1 > int2:
                return 1
        
        return 0