"""
8 7
1 2
1 3
2 4
3 4
5 6
6 7
7 8
"""

def make_set(n):
    p = [i for i in range(n)]
    return p

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[y] = root_x
        for k in range(1, N+1):
            if parents[k] == root_y:
                parents[k] = root_x
    else:
        parents[x] = root_y
        for k in range(1, N+1):
            if parents[k] == root_x:
                parents[k] = root_y

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

parents = make_set(N+1)

for _ in range(M):
    A, B = map(int, input().split())
    union(A, B)
    graph[B].append(A)


print(graph)
print(parents)
