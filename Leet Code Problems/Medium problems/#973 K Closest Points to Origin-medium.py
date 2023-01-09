# import math
# def kClosest(points, k):
#     dist = []
#     ans = []
#     for point in points:
#         dist.append(sqRoot(point))
#     for i in range(len(dist)):
#         for j in range(1,len(dist)):
#             if(dist[j-1]>dist[j]):
#                 print(dist[j-1])
#                 print(dist[j])
#                 print('///')
#                 dist[j-1],dist[j] = dist[j],dist[j-1]
#                 points[j-1],points[j] = points[j],points[j-1]
#     print(points)
#     for i in range(k):
#         # print(points[i])
#         ans.append(points[i])
#     return ans     
# def sqRoot(nums):
#     return math.sqrt((nums[0]**2) +(nums[1]**2))
# res = kClosest([[1,3],[-2,2]],1)
# print(res)
import collections
def kClosest( points, k):
    dist_maps = collections.defaultdict(list)
    ans = []
    for point in points:
        dist = point[0]**2 + point[1]**2
        dist_maps[dist].append([point[0],point[1]])
    sorted_key = sorted(list(dist_maps.keys()))
    print(dist_maps)
    print(sorted_key)

    
    for key in sorted_key:
        if k > 0:
            ans += dist_maps[key]
            k -= len(dist_maps[key])
        else:
            break
    
    return ans
res = kClosest([[1,3],[-2,2]],1)
print(res)