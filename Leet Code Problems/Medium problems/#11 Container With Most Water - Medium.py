def containerWithMostWat(arr):
     l=0
     r= len(arr)-1
     maxArea = 0

     while(l<r):
        maxArea = max(maxArea,min(arr[l],arr[r])*(r-l))
        if (arr[l]<arr[r]):
            l +=1
        else:
            r-=1
     return maxArea


arr = [1,8,6,2,5,4,8,3,7]
res =containerWithMostWat(arr)
print(res)
