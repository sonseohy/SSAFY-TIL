'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def prim(curV):
    U = []
    D = [1e10] * V
    D[curV] = 0

    while len(U) <= V:
        #1. D에서 최선의 값을 고른다.(제일 좋은 vertex = curV)
        minV = 1e10
        for i in range(V):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                curV = i

        U.append(curV)

        #2. D 를 update 한다.
        for i in range(V):
            if i in U: continue
            D[i] = min(D[i], G[curV][i])

    print(U)
    print(D)

V, E = map(int, input().split())
G = [[1e10] * V for _ in range(V)]
for _ in range(E):
    v1, v2, d = map(int, input().split())
    G[v1][v2] = d
    G[v2][v1] = d

prim(0)
