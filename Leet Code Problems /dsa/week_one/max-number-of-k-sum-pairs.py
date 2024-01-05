class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count = Counter(nums)
        ans = 0
        seen = set()
        
        for num in count:
            if num not in seen and k-num in count:
                if num == k-num:
                    ans += count[num]//2
                else:
                    ans += min(count[num],count[k-num])
                seen.add(num)
                seen.add(k-num)
        return ans
                