def findFirstOcurence(nums, target):
    left = 0
    right = len(nums)-1

    while (left < right):
        middle = (left+right)//2
        if (nums[middle] == target):
            if (middle == 0 or nums[middle-1] != target):
                return middle
            right = middle-1
        elif (nums[middle] > target):
            right = middle-1
        else:
            left = middle+1
    return -1


def findLastOcurence(nums, target):
    left = 0
    right = len(nums)-1

    while (left < right):
        middle = (left+right)//2
        if (nums[middle] == target):
            if (middle == len(nums)-1 or nums[middle+1] != target):
                return middle
            left = middle+1
        elif (nums[middle] > target):
            right = middle-1
        else:
            left = middle+1
    return -1


def findFirstAndLastOc(nums, target):
    first = findFirstOcurence(nums, target)
    last = findLastOcurence(nums, target)
    return [first, last]


nums = [1, 2, 11, 11, 11, 45]  # [2,4]
target = 0
res = findFirstAndLastOc(nums, target)
print(res)
