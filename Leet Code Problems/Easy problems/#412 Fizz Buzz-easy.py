class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer =[]
        for l in range(1,n+1):
            if l%3==0 and l%5==0:
                answer.append("FizzBuzz")
            elif l%3 == 0:
                answer.append("Fizz")
            elif l%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(l))
        return answer
                
        