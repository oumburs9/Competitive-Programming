def firstBadVersion(n):
    left = 1
    right = n
    while (left < right):
        mid = left+(right-left)//2
        if (not isBadVersion(mid)):
            left = mid+1
        else:
            right = mid
    return left


def isBadVersion(version):
    first_bad_v = 3
    return version > first_bad_v


res = firstBadVersion(8)
print(res)
