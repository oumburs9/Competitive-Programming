import collections
def kClosest( intervals):
    ans = []
    for i in range(len(intervals)-1):
        if intervals[i][1]>=intervals[i+1][0]:
            ans.append([intervals[i][0],intervals[i+1][1]])
        if intervals[i-1][1]>=intervals[i][0]:
            continue
        ans.append(intervals[i])

res = kClosest([[1,4],[4,5]])
print(res)