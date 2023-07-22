def is_valid_teams(a, b, teams):
    return (a >= teams and b >= teams and a + b - teams * 2 >= teams * 2)

def max_teams(a, b):
    # Binary search 
    left, right = 0, min(a, b)
    max_teams = 0

    while left <= right:
        mid = (left + right) // 2
        if is_valid_teams(a, b, mid):
            max_teams = mid
            left = mid + 1
        else:
            right = mid - 1

    return max_teams

#  test cases
test = int(input())

for _ in range(test):
    a, b = map(int, input().split())  # Read a and b for each test case
    print(max_teams(a, b))  # Print the maximum number of teams for the current test case
