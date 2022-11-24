#  time complexity O(n)
#  space complexity (1)
def moveZeros(nums):

    index = 0
    for num in nums:
        if (num != 0):
            nums[index] = num
            index += 1
    for num in range(index, len(nums)):
        nums[index] = 0
        index += 1

    return nums


array = [1, 0, 0, 3, 45, 44]
print(moveZeros(array))
