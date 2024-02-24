class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize arr with zeros
        stack = []  # Stack to store indices of temperatures in decreasing order of values

        for i in range(n):
            # If the current temperature is higher than the temperature at the top of the stack,
            # update the result for the index at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index

            stack.append(i)  # Push the current index

        return result
