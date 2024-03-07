class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible( weights: List[int], capacity: int, days: int) -> bool:
            days_needed = 1
            current_load = 0
            
            for weight in weights:
                current_load += weight
                if current_load > capacity:
                    days_needed += 1
                    current_load = weight
            
            return days_needed <= days

    
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if isPossible(weights, mid, days):
                right = mid
            else:
                left = mid + 1
        
        return left
