# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

n = int(input())
k = int(input())

adj_list = [[] for _ in range(n + 1)]

# Add an edge 
def add_edge(u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)

# print the vertices adja
def print_adj_vert(u):
    if adj_list[u]:
        print(" ".join(map(str, adj_list[u])))
    else:
        print("")


for _ in range(k):
    op = input().split()
    
    if op[0] == '1':
        u = int(op[1])
        v = int(op[2])
        add_edge(u, v)

    elif op[0] == '2':
        u = int(op[1])
        print_adj_vert(u)

