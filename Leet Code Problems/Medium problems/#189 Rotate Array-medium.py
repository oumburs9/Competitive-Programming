# /**
#  * @param {number[]} nums
#  * @param {number} k
#  * @return {void} Do not return anything, modify nums in-place instead.
#  */
# var rotate = function(nums, k) {
    
  
#   k = k % nums.length;
    
#     reverse(nums, 0, nums.length - 1);
#     reverse(nums, 0, k - 1);
#     reverse(nums, k, nums.length - 1);
    
# };

# let reverse = function(nums, start, end) {
#     while (start < end) {
#         let temp = nums[start];
#         nums[start] = nums[end];
#         nums[end] = temp;
#         start++;
#         end--;
#     } 
    
# };


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

