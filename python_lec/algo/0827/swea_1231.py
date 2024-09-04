def inorder(root_idx):
    if root_idx <= N:
        inorder(root_idx*2)
        result.append(TREE[root_idx])
        inorder(root_idx*2 + 1)

T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    TREE = [[] for _ in range(N+1)]
    root_idx = 1

    for i in range(N):
        TREE[int(arr[i][0])] = arr[i][1]

    result = []
    inorder(root_idx)
    print(f'#{test_case}', "".join(result))
