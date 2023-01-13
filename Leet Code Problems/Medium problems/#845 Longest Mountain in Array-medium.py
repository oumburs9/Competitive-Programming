# class Solution:
#     def longestMountain(self, arr: List[int]) -> int:
#          l = len(arr)
#          ans = 0
#          i =0

#         #  for i in range(l-1):
#          while i <= l-1:
#             if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#                 count = 1
#                 j = i

#                 while (j>0 and arr[j]>arr[j-1]):
#                     j-=1
#                     count +=1

#                 while (i<l-1 and arr[i]>arr[i+1]):
#                     count +=1
#                     i+=1
#             else:
#                 i +=1
            
#                 ans = max(ans,count)
#          return ans



from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
    
        N = len(arr)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and arr[end] < arr[end + 1]: 
                
                while end+1 < N and arr[end] < arr[end+1]:
                    end += 1

                if end + 1 < N and arr[end] > arr[end + 1]: 
                    while end+1 < N and arr[end] > arr[end+1]:
                        end += 1
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans



        
        
        
        