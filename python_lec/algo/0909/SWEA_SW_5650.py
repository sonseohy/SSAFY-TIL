def block(b, k):  # block을 만났을 때 진행방향을 바꿔줌
    if k == 0:  # 진행방향이 오른쪽일 때
        if b == 3:  # block 3을 만나면 진행방향을 아래로
            return 1
        elif b == 4:  # block 4를 만나면 진행방향을 위로
            return 3
        else:  # block 1, 2, 5를 만나면 진행방향을 왼쪽으로
            return 2
    elif k == 1:  # 진행방향이 아래일 때
        if b == 1:
            return 0
        elif b == 4:
            return 2
        else:  # block 2, 3, 5를 만나면 진행방향을 왼쪽으로
            return 3
    elif k == 2:  # 진행방향이 왼쪽일 때
        if b == 1:
            return 3
        elif b == 2:
            return 1
        else:  # block 3, 4, 5를 만나면 진행방향을 왼쪽으로
            return 0
    else:  # 진행방향이 위일 때
        if b == 2:
            return 0
        elif b == 3:
            return 2
        else:  # block 1, 4, 5를 만나면 진행방향을 왼쪽으로
            return 1

def wormholes(w_id, ni, nj):
    for wi in range(N):
        for wj in range(N):
            if BOARD[wi][wj] == w_id and (wi != ni or wj != nj):
                return wi, wj
        else:
            continue
        return

def pinball(sti, stj, k):
    global max_score
    score = 0
    st_r, st_c = sti, stj
    di = [0, 1, 0, -1]  # 우 하 좌 상
    dj = [1, 0, -1, 0]

    visited = set()  # (row, col, direction) 조합을 기록하여 사이클 방지

    while True:
        if (sti, stj, k) in visited:
            break  # 사이클 발견, 루프 종료
        visited.add((sti, stj, k))

        ni = sti + di[k]
        nj = stj + dj[k]

        if not (0 <= ni < N and 0 <= nj < N):  # 벽에 부딪힌 경우
            k = (k + 2) % 4
            score += 1
            ni = sti + di[k]
            nj = stj + dj[k]

        if ni == st_r and nj == st_c:  # 출발 위치에 돌아온 경우
            max_score = max(max_score, score)
            return

        if BOARD[ni][nj] == -1:  # 블랙홀에 빠진 경우
            max_score = max(max_score, score)
            return

        if 6 <= BOARD[ni][nj] <= 10:  # 웜홀 처리
            wormhole_id = BOARD[ni][nj]
            ni, nj = wormholes(wormhole_id, ni, nj)


        if 1 <= BOARD[ni][nj] <= 5:  # 블록 처리
            sti, stj = ni, nj
            k = block(BOARD[ni][nj], k)
            score += 1
        else:  # 빈 공간 처리
            sti, stj = ni, nj


T = int(input())

for test_case in range(1, T + 1):
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