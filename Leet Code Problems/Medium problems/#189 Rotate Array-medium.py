class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n
        if k == 0:
            return

        rotated = [0] * n
        for i in range(n):
            rotated[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = rotated[i]


        


def rotate(nums,k):
    k = k%len(nums)
    def reverse(nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[start] , nums[end] 
            start +=1
            end -=1
    
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

