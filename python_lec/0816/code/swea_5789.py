T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]

    box = [0] * (N+1)

    idx = 1
    for l, r in arr:
        for i in range(l, r+1):
            box[i] = idx
            print(box)
        idx += 1


    print(f'#{test_case}', *box[1:])