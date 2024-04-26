# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

class DisjointSets:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        
        # keep
        self.min_el = list(range(n + 1))
        self.max_el = list(range(n + 1))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
            
        return self.parent[u]



    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        
        if u_root != v_root:
            # update the u_root to grt
            if self.size[u_root] < self.size[v_root]:
                u_root, v_root = v_root, u_root
                
            self.parent[v_root] = u_root
            self.size[u_root] += self.size[v_root]
            
            # update the min, max of u_
            self.min_el[u_root] = min(self.min_el[u_root], self.min_el[v_root])
            self.max_el[u_root] = max(self.max_el[u_root], self.max_el[v_root])
            

            
    def get(self, v):
        root = self.find(v)
        return self.min_el[root], self.max_el[root], self.size[root]


n, m = map(int, input().split())
disu = DisjointSets(n)
for _ in range(m):
    qry = input().split()
    
    # if the queries
    if qry[0] == 'union':
        u, v = map(int, qry[1:])
        disu.union(u, v)
    elif qry[0] == 'get':
        # finsd v
        v = int(qry[1])
        
        result = disu.get(v)
        print(*result)