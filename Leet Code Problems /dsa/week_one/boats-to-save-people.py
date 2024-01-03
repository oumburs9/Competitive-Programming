class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        num_bot = 0
        while(left <= right):
            if(left == right):
                num_bot += 1
                break
            if(people[left]+people[right] <= limit):
                left +=1
            right -=1
            num_bot += 1
        return num_bot
            
