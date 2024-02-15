class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 10 and fives >= 1:
                fives -= 1
                tens += 1
            elif bill == 20 and tens >= 1 and fives >= 1:
                fives -= 1
                tens -= 1
            elif bill == 20 and fives >= 3:
                fives -= 3
            elif bill == 5:
                fives += 1
                continue
            else: 
                return False

        return True
            

        