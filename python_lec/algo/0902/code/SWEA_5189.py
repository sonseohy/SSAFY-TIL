def recur(level):
    if level == N+1:
        return

    for i in range(2, N+1):
        if i in path:
            print(*path)
            continue
        path.append(i)
        recur(level+1)
        path.pop()

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    BATTERY = [list(map(int, input().split())) for _ in range(N)]

    path = []
    path.append(1)
    recur(1)

    # print(f'#{test_case} {}')