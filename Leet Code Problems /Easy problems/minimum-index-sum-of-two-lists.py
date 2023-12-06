class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1Dic = {}
        list2Dic = {}
        res = []

        for i in range(max(len(list1),len(list2))):
            if len(list1) > i:
                list1Dic[list1[i]] = i
            if len(list2) > i:
                list2Dic[list2[i]] = i
            
        minS = float('inf')
        for i, v in list1Dic.items():
            if i in list2Dic:
                curS = v + list2Dic[i]
                if curS < minS:
                    minS = curS
                    res = [i]
                elif curS == minS:
                    res.append(i)
                    

        return res
