
def subsets(nums):
    ans = []
    cur = []
    solution(nums, ans, cur, 0)
    return ans


def solution(nums, ans, cur, index):
    if (index > len(nums)):
        return
    ans.append(cur[:])
    for i in range(index, len(nums)):
        if (nums[i] not in cur):
            cur.append(nums[i])
            solution(nums, ans, cur, i)
            cur.pop()
    return
