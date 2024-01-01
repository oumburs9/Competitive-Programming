
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_maps = collections.defaultdict(list)
        ans = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)
            dist_maps[dist].append([point[0],point[1]])
        sorted_key = sorted(list(dist_maps.keys()))
        
        for key in sorted_key:
            if k > 0:
                ans += dist_maps[key]
                k -= len(dist_maps[key])
            else:
                break
        
        return ans
        