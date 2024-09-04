def preorder(root_idx):
    if root_idx <= N:
        preorder(root_idx*2)
        lst.append(TREE[root_idx])
        preorder(root_idx*2+1)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    TREE = [0] * (N+1)
    for i in range(1, N+1):
        TREE[i] = i


    lst = []
    root = 1
    preorder(root)

    for j in range(N):
        TREE[lst[j]] = j + 1

    print(f'#{test_case} {TREE[root]} {TREE[N//2]}')