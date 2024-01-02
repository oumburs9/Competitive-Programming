class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        _dict = defaultdict(int)

        for i,v in enumerate(numbers):
            if v in _dict:
                return [_dict[v]+1, i+1 ]
            _dict[target-v] = i
        

        