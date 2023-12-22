class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest_so_far = float('inf')
        second_smallest_so_far = float('inf')
        
        for num in nums:
            if num <= smallest_so_far:
                smallest_so_far = num
            elif num <= second_smallest_so_far:
                second_smallest_so_far = num
            else:
                return True
        
        return False
