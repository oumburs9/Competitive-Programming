def numRescueBoats(people, limit):
    people.sort()

    left = 0
    right = len(people)-1

    boats_number = 0

    while (left <= right):
        if (left == right):
            boats_number += 1
            break
        if (people[left]+people[right] <= limit):
            left += 1

        right -= 1
        boats_number += 1
    return boats_number


people = [4, 6, 11, 19, 9]
limit = 19
print(numRescueBoats(people, limit))
