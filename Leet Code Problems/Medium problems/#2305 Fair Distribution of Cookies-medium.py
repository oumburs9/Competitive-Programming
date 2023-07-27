class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        minUnfairness = float('inf')

        def backtrack(i, bucket):
            nonlocal minUnfairness

            # Base case: If all cookies are distributed, update the minimum unfairness
            if i >= len(cookies):
                minUnfairness = min(minUnfairness, max(bucket))
                return

            # Pruning case: If the current distribution is already worse than the minimum unfairness, stop exploring
            if max(bucket) > minUnfairness:
                return

            # Try assigning the i-th cookie to each child and explore the possibilities
            for j in range(k):
                bucket[j] += cookies[i]  # Assign cookie to the j-th child
                backtrack(i + 1, bucket)  # Explore next cookie
                bucket[j] -= cookies[i]  # Backtrack: Remove cookie from the j-th child

        backtrack(0, bucket)  # Start the backtracking process with initial index and bucket
        return minUnfairness
