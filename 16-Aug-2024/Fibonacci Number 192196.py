# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def __init__(self):
        self.memo = {}
    def fib(self, n: int) -> int:
        if n == 0 or n == n == 1:
            return n
        if n not in self.memo:
            self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.fib(n - 1) + self.fib(n - 2)