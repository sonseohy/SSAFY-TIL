T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(M)]

    TREE = [0] * (N+1)
    last = N
    for i in range(M):
        TREE[nodes[i][0]] = nodes[i][1]

    for j in range(last, 0, -1):
        if TREE[j] == 0:
            if j*2 <= N and TREE[j*2] != 0:
                TREE[j] += TREE[j*2]
            if j*2+1 <= N and TREE[j*2+1] != 0:
                TREE[j] += TREE[j*2+1]

    print(f'#{test_case} {TREE[L]}')