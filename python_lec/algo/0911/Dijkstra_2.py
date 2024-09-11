'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 6
'''

def dijk(curV):
    U = []
    D = [1e10] * V
    D[curV] = 0

    while len(U) <= V:
        # 1
        minV = 1e10
        for i in range(V):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                curV = i

        # 2
        U.append(curV)

        # 3 D를 update
        for i in range(V):
            if i in U: continue
            D[i] = min(D[i], D[curV]+G[curV][i])

    print(D)
    print(U)


V, E = map(int, input().split())
G = [[1e10] * V for _ in range(V)]
for _ in range(E):
    v1, v2, d = map(int, input().split())
    G[v1][v2] = d

# print(G)
dijk(0)
