T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    for i in range(N):
        w_cnt = 0
        b_cnt = 0
        r_cnt = 0
        for j in range(M):
            if i == 0 and arr[i][j] != 'W':
                arr[i][j] = 'W'
                cnt += 1
            elif i == N-1 and arr[i][j] != 'R':
                arr[i][j] = 'R'
                cnt += 1
            else:
                if arr[i][j] == 'W':
                    w_cnt += 1
                elif arr[i][j] == 'B':
                    b_cnt += 1
                elif arr[i][j] == 'R':
                    r_cnt
        if arr[i-1][0] == 'W':   # 'W' or 'B'
            if w_cnt > b_cnt:
                for k in range(M):
                    if arr[i][k] != 'W':
                        arr[i][k] = 'W'
                        cnt += 1
            else:
                for k in range(M):
                    if arr[i][k] != 'B':
                        arr[i][k] = 'B'
                        cnt += 1
        elif arr[i-1][0] == 'B':  # 'B' or 'R'
            if b_cnt > r_cnt:
                for k in range(M):
                    if arr[i][k] != 'B':
                        arr[i][k] = 'B'
                        cnt += 1
            else:
                for k in range(M):
                    if arr[i][k] != 'R':
                        arr[i][k] = 'R'
                        cnt += 1
        print(arr, cnt)
    print(f'#{test_case} {cnt}')