class Solution:
   def hIndex(self, citations: List[int]) -> int:
        # citations.sort() since its guarenteed to be sorted
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            h = n - mid
            
            if citations[mid] >= h:
                right = mid - 1
            else:
                left = mid + 1

        return n - left