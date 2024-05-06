# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        currentXor = 0
        for num in nums:
            currentXor ^= num
        targetXor = currentXor ^ k
        
        if targetXor == 0:
            return 0
        
        bit_count = defaultdict(int)
        
        for num in nums:
            mask = num ^ targetXor
            for i in range(20):  
                if mask & (1 << i):
                    bit_count[i] += 1  
        
        min_operations = float('inf')
        for num in nums:
            operations = 0
            for i in range(20):  
                if targetXor & (1 << i):  
                    if (num & (1 << i)) == 0:
                        operations += 1 
                    else:
                        operations += 1 
            min_operations = min(min_operations, operations)
        
        return min_operations