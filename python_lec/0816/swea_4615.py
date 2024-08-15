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

    # 돌을 놓을 수 있는 곳 : 흑의 경우 W의 상하좌우 빈 곳
    # 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]