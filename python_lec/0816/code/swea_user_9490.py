T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_v = 0
    for i in range(N):
        for j in range(M):
            sum_v = arr[i][j]
            for b in range(1, arr[i][j]+1):
                for k in range(4):
                    ni = i+di[k] * b
                    nj = j+dj[k] * b
                    if 0 <= ni < N and 0 <= nj < M:
                        sum_v += arr[ni][nj]

            if max_v < sum_v:
                max_v = sum_v

    print(f'#{test_case} {max_v}')


"""
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    k = 0
    max_v = arr[0][0]

    for n in range(N):
        for m in range(M):
            sum_v = arr[n][m]
            for mul in range(1, sum_v + 1):
                for k in range(4):
                    newR = n + dr[k] *mul
                    newC = m + dc[k] * mul
                    if (newR >= 0 and newR < N) and (newC >= 0 and newC < M):
                        sum_v += arr[newR][newC]

            if max_v < sum_v:
                max_v = sum_v

    print(f'#{test_case} {max_v}')
"""