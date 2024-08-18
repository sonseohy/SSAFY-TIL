# 흑돌 : 1, 백돌 : 2
# N은 4, 6, 8 중 하나
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    OTHELLO = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * N for _ in range(N)]

    op = [0, 'W', 'B']  # 흑돌과 백돌의 인덱스에 반대색 저장
    wb = [0, 'B', 'W']

    # 초기 setting
    for idx in range(2):
        board[N//2-idx][N//2-idx] = 'W'
        board[N//2-idx][N//2-1+idx] = 'B'

    di = [-1, 0, 1, 0, 1, 1, -1, -1]
    dj = [0, 1, 0, -1, 1, -1, 1, -1]

    for y, x, s in OTHELLO:
        board[x-1][y-1] = wb[s]     # 돌을 놓는 위치
        for k in range(8):
            ni = (x-1) + di[k]
            nj = (y-1) + dj[k]
            tmp = []
            while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[s]:
                tmp.append([ni, nj])
                ni += di[k]
                nj += dj[k]

            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == wb[s]:
                for ti, tj in tmp:
                    board[ti][tj] = wb[s]

    # for i in range(N):
    #     print(*board[i])

    b_cnt = 0
    w_cnt = 0
    for i in board:
        for j in i:
            if j == 'B':
                b_cnt += 1
            elif j == 'W':
                w_cnt += 1
    
    print(f'#{test_case} {b_cnt} {w_cnt}')

# 오답
# 마지막 b, c 카우늩에서 if == 'B' 와 else로 쓰면 통과 못함
