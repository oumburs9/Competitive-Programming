def missing(arr):
    arr.sort()
    length = len(arr)
    for i in range(len(arr)-1):
        if(arr[i]+1 != arr[i+1]):
            return arr[i]+1
        i+=1


# arr = [1,2,0,4]
# print(missing(arr))

def missingGauss(arr):
    arr.sort()
    arrn = []
    for i in range(arr[-1]):
        arrn.append(i+1)
        print(arrn)
    
    return sum(arrn) - sum(arr)
# print(missingGauss([1,2,3,5]))


def missingNumberGauss(arr):
    currentSum = sum(arr)
    n = len(arr)
    supposedSum = n*(n+1)/2
    return int(supposedSum - currentSum)

res = missingNumberGauss([1,2,4,5,6,0])
# res = missingNumberGauss([3,0,1])
print(res)

