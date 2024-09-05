def change_battery(stop, charge, cnt):
    global result
    if stop == N-1:
        if result > cnt:
            result = cnt
        return

    if cnt > result:
        return

    for i in range(BATTERY[stop]):
        if visited[i] == 1:
            continue
        cnt += 1
        visited[i] = 1
        change_battery(i+1, charge+BATTERY[i], cnt)
        cnt -= 1
        visited[i] = 0

T = int(input())

for test_case in range(1, T+1):
    info = list(map(int, input().split()))
    N = info[0]
    BATTERY = info[1:]

    result = 10001
    visited = [0] * (N-1)
    change_battery(0, 0, 0)
    print(f'#{test_case} {result}')