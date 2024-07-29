# Problem: A - Valid Parentheses - https://codeforces.com/gym/537575/problem/A

s = input()
stack = []
valid_count = 0

for char in s:
    if char == '(':
        stack.append(char)
    elif char == ')' and stack:
        stack.pop()
        valid_count += 2
        
print(valid_count)