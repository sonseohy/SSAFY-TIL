import sys
sys.stdin = open('input.txt', 'r')

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

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    parents = make_set(N+1)

    for p1, p2 in arr:
        union(p1, p2)

    print(f'#{test_case} {len(set(parents))-1}')