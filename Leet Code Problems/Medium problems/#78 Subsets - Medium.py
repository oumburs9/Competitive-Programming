
# def subsets(nums):
#     ans = []
#     cur = []
#     solution(nums, ans, cur, 0)
#     return ans


# def solution(nums, ans, cur, index):
#     if (index > len(nums)):
#         return
#     ans.append(cur[:])
#     for i in range(index, len(nums)):
#         if (nums[i] not in cur):
#             cur.append(nums[i])
#             solution(nums, ans, cur, i)
#             cur.pop()
#     return


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current, idx):
            if idx == len(nums):
                result.append(current.copy())
                return

            # Take the decision to include the current number
            current.append(nums[idx])
            backtrack(current, idx + 1)
            current.pop()  # Backtrack and remove the current number

            # Take the decision not to include the current number
            backtrack(current, idx + 1)

        backtrack([], 0)

        return result
