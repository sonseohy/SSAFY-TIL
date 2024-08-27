def preorder(root):
    global cnt
    cnt += 1
    for c in TREE[root]:
        preorder(c)
    return cnt

T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    num = list(map(int, input().split()))

    cnt = 0
    TREE = [[] for _ in range(E+2)]
    for i in range(0, len(num), 2):
        v1 = num[i]
        v2 = num[i+1]

        TREE[v1].append(v2)
    print(f'#{test_case} {preorder(N)}')