class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prefixSums = {}
        for (i, num) in enumerate(nums):
            if num not in prefixSums:
                prefixSums[num] = [1, [i]]
            else:
                prefixSums[num][0] += 1
                prefixSums[num][1].append(prefixSums[num][1][-1] + i)
        distances = []
        for (i, num) in enumerate(nums):
            n = len(prefixSums[num][1])
            if n == 1:
                distances.append(0)
            else:
                prefixSum = prefixSums[num][1]
                k = n - prefixSums[num][0] 
                left, right = prefixSum[k] - i, prefixSum[-1] - prefixSum[k]
                mid = (2*k - n + 1)*i
                distances.append(right - left + mid)
                prefixSums[num][0] -= 1
        return distances