# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                # If the mid version is bad, the first bad version is to the left.
                right = mid
            else:
                # If the mid version is not bad, the first bad version is to the right.
                left = mid + 1

        return left
        


# def firstBadVersion(n):
#     left = 1
#     right = n
#     while (left < right):
#         mid = left+(right-left)//2
#         if (not isBadVersion(mid)):
#             left = mid+1
#         else:
#             right = mi
#     return left


# def isBadVersion(version):
#     first_bad_v = 3
#     return version > first_bad_v


# res = firstBadVersion(8)
# print(res)
