# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/547609/problem/B

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
                
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
                
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
                
n = int(input())

distant_rel = list(map(int, input().split()))

uf = UnionFind(n)
for i in range(n):
    
    uf.union(i, distant_rel[i] - 1)  
    
    # print(i,distant_rel[i] - 1)

# cnt uniq rts
unique_rts = len( set( uf.find(x) for x in range(n) ))
print(unique_rts)