class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Dict = defaultdict(int)
        lenArr1 = len(arr1) 

        for i , v in enumerate(arr2):
            arr2Dict[v] = i

        def relativeSort(x):
            if x in arr2Dict:
                return arr2Dict[x]
            return x + lenArr1

        arr1.sort(key = relativeSort)
        return arr1
        '''
{
    2: 0,
    1: 1,
    4: 2
}
        '''



        
        