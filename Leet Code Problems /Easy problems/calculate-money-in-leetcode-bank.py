class Solution:
    def totalMoney(self, n: int) -> int:
        no_week = n // 7
        remain_day = n % 7

        total =  ((no_week*(no_week-1)) //2 )*7
        total += no_week*28
        total += ((remain_day * (remain_day + 1)) //2) + (no_week * remain_day) 

        return total
   

            
        