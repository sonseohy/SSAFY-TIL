import sys
sys.stdin = open('input.txt', 'r')

"""
반례
1
6 4
1 3 2 6 5 6 3 6
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
        # 그룹들이 묶일 때 해당 그룹의 모든 상위 노드를 바꾸어 주어야 함
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
    group = list(map(int, input().split()))

    parents = make_set(N+1)
    for i in range(0, M*2, 2):
        union(group[i], group[i+1])
    print(parents)
    print(f'#{test_case} {len(set(parents))-1}')