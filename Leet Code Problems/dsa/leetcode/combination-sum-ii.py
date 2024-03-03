class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:    
        def solution(candidates, ans, cur, target, index, summation):
            if summation == target:
                ans.append(cur[:])
            elif summation < target:
                n = len(candidates)
                for i in range(index, n):
                    # skip dupli
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    cur.append(candidates[i])
        
                    solution(candidates, ans, cur, target, i + 1, summation + candidates[i])
                    cur.pop()

        candidates.sort() 
        ans = []
        cur = []
        solution(candidates, ans, cur, target, 0, 0)
        return ans
