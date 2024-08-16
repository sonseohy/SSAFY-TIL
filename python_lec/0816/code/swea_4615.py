# 흑돌 : 1, 백돌 : 2
# N은 4, 6, 8 중 하나
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    OTHELLO = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * N for _ in range(N)]

    # 초기 setting
    for idx in range(2):
        board[N//2-idx][N//2-idx] = 'W'
        board[N//2-idx][N//2-1+idx] = 'B'

    di = [-1, 0, 1, 0, 1, 1, -1, -1]
    dj = [0, 1, 0, -1, 1, -1, 1, -1]

    black = 0
    white = 0
    for y, x, s in OTHELLO:
        board[x - 1][y - 1] = s
        for k in range(8):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 'W' and s == 1:
                    board[ni][nj] = 'B'
                    black += 1
                elif board[ni][nj] == 'B' and s == 2:
                    board[ni][nj] = 'W'
                    white += 1

    print(f'#{test_case} {black} {white}')