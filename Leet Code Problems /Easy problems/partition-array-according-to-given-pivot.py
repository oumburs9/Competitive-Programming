class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        great = []

        for num in nums:
            if num > pivot:
                great.append(num)
            elif num < pivot:
                less.append(num)

        numPiv = len(nums) - (len(less) + len(great)) 
        return less + [pivot]*numPiv + great
        