def pancakeSort(arr):
    

    l = 0
    ans = arr
    ans.reverse()
    print(ans)
    print(arr)

    # while l<=(len(arr)-1):
    #    ans += arr[:arr[l-1]]
    #    break
    #    l+=1
    # ans = arr[:arr[0]]+ arr[arr[0]:]
    
    return ans


res = pancakeSort([3,2,4,1])
# print(res)