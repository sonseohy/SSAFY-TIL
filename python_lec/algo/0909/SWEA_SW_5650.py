def block(b, k):    # block을 만났을 때 진행방향을 바꿔줌
    if k == 0:  # 진행방향이 오른쪽일 때
        if b == 3:    # block 3을 만나면 진행방향을 아래로
            return 1
        elif b == 4:    # block 4를 만나면 진행방향을 위로
            return 3
        else:           # block 1, 2, 5를 만나면 진행방향을 왼쪽으로
            return 2
    elif k == 1:    # 진행방향이 아래일 때
        if b == 1:
            return 0
        elif b == 4:
            return 2
        else:           # block 2, 3, 5를 만나면 진행방향을 왼쪽으로
            return 3
    elif k == 2:    # 진행방향이 왼쪽일 때
        if b == 1:
            return 3
        elif b == 2:
            return 1
        else:           # block 3, 4, 5를 만나면 진행방향을 왼쪽으로
            return 0
    else:   # 진행방향이 위일 때
        if b == 2:
            return 0
        elif b == 3:
            return 2
        else:           # block 1, 4, 5를 만나면 진행방향을 왼쪽으로
            return 1

def pinball(sti, stj, k):
    global max_score
    score = 0
    st_r, st_c = sti, stj
    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while True:
        ni = sti + di[k]
        nj = stj + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if ni == st_r and nj == st_c:   # 핀볼이 출발 위치에 돌아왔을 때
                max_score = max(max_score, score)
                return
            if BOARD[ni][nj] == -1:     # 블랙홀을 만났을 때
                max_score = max(max_score, score)
                return
            if 6 <= BOARD[ni][nj] <= 10:  # 웜홀을 만났을 때
                for wi in range(N):
                    for wj in range(N):
                        if BOARD[wi][wj] == BOARD[ni][nj] and (wi != ni or wj != nj):
                            sti, stj = wi, wj
                            break
                    else:
                        continue
                    break

            if 1 <= BOARD[ni][nj] <= 5:     # 블록을 만났을 때
                sti, stj = ni, nj
                k = block(BOARD[ni][nj], k)
                if sti + di[k] < 0 or stj + dj[k] < 0:
                    return
                score += 1
            if BOARD[ni][nj] == 0:   # 빈공간일 때
                sti, stj = ni, nj
        else:   # 벽을 만났을 때
            k = (k+2) % 4   # 상하좌우 변경
            score += 1

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    BOARD = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 상하좌우
    # start 지점 찾기
    for r in range(N):
        for c in range(N):
            if BOARD[r][c] == 0:
                for i in range(4):
                    if 0 <= r + d[i][0] < N and 0 <= c + d[i][1] < N:
                        pinball(r, c, i)

    print(f'#{test_case} {max_score}')