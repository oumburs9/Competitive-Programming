class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        minUnfairness = float('inf')

        def backtrack(i, bucket):
            nonlocal minUnfairness

            # Base case: 
            if i >= len(cookies):
                minUnfairness = min(minUnfairness, max(bucket))
                return

            # Pruning case: 
            if max(bucket) > minUnfairness:
                return

            # assigning the i-th cookie to each child and explore the possibilities
            for j in range(k):
                bucket[j] += cookies[i]  # Assign cookie to the j-th child
                backtrack(i + 1, bucket)  # Explore next
                bucket[j] -= cookies[i]  # Backtrack: 

        backtrack(0, bucket)  # Start the backtracking 
        return minUnfairness
