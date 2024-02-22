class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums1)

        idxDict = { n : i   for  i,n in enumerate(nums1)}


        for i in range(len(nums2)):

            while stack and nums2[i] > stack[-1]:
                idx =  idxDict[stack.pop()]

                res[idx] =  nums2[i]
            if nums2[i] in idxDict:
                stack.append(nums2[i])

        return res
     
        
        
        
        

        