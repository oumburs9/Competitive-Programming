class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        counter = 0
        sum_dict = {}

        for i in range(len(nums)):
            total += nums[i]

            # Check if the current total is equal to k
            if total == k:
                counter += 1

            # Check if there is a subarray whose sum is (total - k)
            if (total - k) in sum_dict:
                counter += sum_dict[total - k]

            # Update the dictionary with the current total
            if total in sum_dict:
                sum_dict[total] += 1
            else:
                sum_dict[total] = 1

        return counter
