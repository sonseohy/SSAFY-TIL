def min_heap(num):
    global last

    last += 1
    TREE[last] = num
    c = last
    p = c//2
    while p >= 1 and TREE[p] > TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        # 오답 point : 부모 노드와 자식 노드를 바꿔줘야함
        c = p
        p = c//2

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    TREE = [0] * (N+1)
    last = 0
    for num in numbers:
        min_heap(num)

    sum_v = 0
    while N > 0:
        N //= 2
        sum_v += TREE[N]
    print(f'#{test_case} {sum_v}')