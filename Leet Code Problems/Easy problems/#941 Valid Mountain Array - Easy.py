def validMountain(arr):
    if (len(arr) < 3):
        return False
    index = 1
    while (index < len(arr) and arr[index] > arr[index-1]):
        index += 1
    if (index == 1 or index == len(arr)):
        return False
    while (index < len(arr) and arr[index] < arr[index-1]):
        index += 1
    return index == len(arr)


arr = [1, 2, 3, 8, 6, 9]
print(validMountain(arr))
