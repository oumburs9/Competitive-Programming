# Problem: B - Make it Divisible by 25 - https://codeforces.com/gym/543262/problem/B

t = int(input())
for _ in range(t):
    n = input()

    length = len(n)

    min_steps = float('inf')
    
 
    targets = ['00', '25', '50', '75']
    
    for target in targets:
        pos = len(target) - 1
        count = 0
        for i in range(length - 1, -1, -1):

            if n[i] == target[pos]:
                pos -= 1

                if pos < 0:
                    break
            else:
                count += 1
        
        if pos < 0:

            min_steps = min(min_steps, count)

    
    print(min_steps)
