# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

def count(n, matrix):
    cnt_road = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                cnt_road += 1
        
    return cnt_road

# input matri
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

cnt_road = count(n, matrix)

print(cnt_road//2)