def calculator(left, right, op):
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        return left // right

T = 10

for test_case in range(1, T+1):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]

    TREE = [0] * (N+1)

    for k in range(N):
        if nodes[k][1].isdigit():
            TREE[int(nodes[k][0])] = int(nodes[k][1])
        else:
            TREE[int(nodes[k][0])] = nodes[k][1]

    for i in range(N, 0, -1):
        if len(nodes[i-1]) > 2:
            cal_v = calculator(TREE[int(nodes[i-1][2])], TREE[int(nodes[i-1][3])], TREE[i])
            TREE[i] = cal_v

    print(f'#{test_case} {TREE[1]}')


'''
def postorder(root):
    if TREE[root][0].isdigit():
        return int(TREE[root][0])
    else:
        v1 = postorder(int(TREE[root][1]))
        v2 = postorder(int(TREE[root][2]))
        if ...
        return v1 + v2

T = 1

for test_case in range(1, T+1):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]
    
    TREE = [[] for _ in range(N+1)]
    for _ in range(N):
        arr = input().split()
        no = int(arr[0])
        TREE[no] = arr[1:]

    print()
'''