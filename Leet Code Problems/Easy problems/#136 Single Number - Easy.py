def singleNumber(arr):
    arr.sort()

    for i in range(0,len(arr)-1,2):
        if(arr[i] !=arr[i+1]):
            return arr[i]
        


# res = singleNumber([1,1,3,3,5,6,6])
# print(res)

def singleNum(arr):
    return sum(set(arr))*2-sum(arr)

res = singleNum([1,1,2,2,5,6,6])
print(res)
        

