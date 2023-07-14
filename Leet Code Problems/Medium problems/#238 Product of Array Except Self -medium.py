from ast import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Calculate prefix product
        prefix = 1
        for i in range(n):
            # Store the current prefix product in the result array
            result[i] = prefix
            # Update the prefix product for the next element
            prefix *= nums[i]

        # Calculate suffix product and construct result array
        suffix_product = 1
        for i in range(n-1, -1, -1):
            # Multiply the current suffix product with the corresponding element in the result array
            result[i] *= suffix_product
            # Update the suffix product for the next element
            suffix_product *= nums[i]

        return result

            
            
        

# from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res
            
            
            
                
        