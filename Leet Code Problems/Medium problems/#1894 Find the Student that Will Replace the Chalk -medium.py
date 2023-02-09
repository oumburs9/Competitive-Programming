from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_ = sum(chalk)
        max_ = k % sum_
       
        for i in range(len(chalk)):
            if max_-chalk[i] >= 0:
                max_ -= chalk[i]
            else:
                return i 
        return i
                