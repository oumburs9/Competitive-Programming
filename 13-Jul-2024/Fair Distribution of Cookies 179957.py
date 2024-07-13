# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        minUnfairness = float('inf')

        def backtrack(i, bucket):
            nonlocal minUnfairness

            if i >= len(cookies):
                minUnfairness = min(minUnfairness, max(bucket))
                return

           
            if max(bucket) > minUnfairness:
                return

            for j in range(k):
                bucket[j] += cookies[i] 
                backtrack(i + 1, bucket) 
                bucket[j] -= cookies[i]  

        backtrack(0, bucket)
        return minUnfairness
