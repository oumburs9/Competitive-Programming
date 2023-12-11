class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_dict = defaultdict(list)

        for i, num in enumerate(nums):
            index_dict[num].append(i)

        for old, new in operations:
            
            if old in index_dict:
                for index in index_dict[old]:
                    nums[index] = new

                index_dict[new] = index_dict.pop(old)

        return nums
