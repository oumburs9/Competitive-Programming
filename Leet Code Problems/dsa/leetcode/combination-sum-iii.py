class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def solution(cur, index, _sum):
            if len(cur) == k and _sum == n:
                ans.append(cur[:])

            elif len(cur) < k and _sum < n:
                # ..
                for i in range(index, 10):
                    cur.append(i)

                    solution(cur, i + 1, _sum + i)

                    cur.pop()

        ans = []
        solution([], 1, 0)
        return ans
