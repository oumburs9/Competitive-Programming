# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

def adj_matri_to_list(n, matrix):
    adj_list = []

    for i in range(n):
        neighbors = []

        for j in range(n):
            if matrix[i][j] == 1:
                neighbors.append(j + 1)
        adj_list.append((len(neighbors), neighbors))
        
    return adj_list

# input matri
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

#call the adj
adj_list = adj_matri_to_list(n, matrix)

for edges, neighbors in adj_list:
    print(edges, " ".join(map(str, neighbors)))