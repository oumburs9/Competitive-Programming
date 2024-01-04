class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        res = 0

        while left < right:
            if skill[left] + skill[right] != skill[left + 1 ] + skill[right - 1 ]:
                return -1
            else:
                res += skill[left] * skill[right]
                left += 1
                right -= 1
        return res
        

        