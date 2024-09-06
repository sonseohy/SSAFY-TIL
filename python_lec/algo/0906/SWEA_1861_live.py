import sys
sys.stdin = open('input.txt', 'r')

# 접근방법 2
# 1. 전체 배열을 순회하면서 확인한다.
# 2. 인접한 방의 숫자가 현재 방보다 1 크면 visited 1 체크
# - 1이 크면 다음으로 갈 수 있다
# 정리 : 다음으로 갈 수 있는 방이다라는 정보를 저장

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ROOMS = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * (N * N + 1) # index 에러 조심
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 전체를 순회하며 상하좌우에 나보다 1이 크다면, visited 체크
    for i in range(N):
        for j in range(N):
            for k in range(4):
                # ny, nx = 다음 좌표
                ni = i + di[k]
                nj = j + dj[k]
                # 범위 체크
                if ni < 0 or nj >= N or nj < 0 or ni >= N:
                    continue
                # 내 옆이 나보다 1 크다면 나는 다음으로 갈 수 있는 방이다.
                if ROOMS[ni][nj] == ROOMS[i][j] + 1:
                    visited[ROOMS[i][j]] = 1
                    # 이미 체크된 순간, 다른 방향은 볼 필요가 없음
                    # 이유 : 동일한 숫자가 없기 때문에, 나보다 1 큰 경우는 하나밖에 없음
                    break
    # cnt : 하나씩 체크 / max_cnt : 정답(최대값) / start : 계산을 시작할 위치
    cnt = max_cnt = start = 0

    # 앞에서부터 하면 실수 가능성 높은 문제 : 뒤에서부터 보기
    for i in range(N*N - 1, -1, -1): # 앞에서부터 보면 마지막 방 번호가 들어가기 때문
        if visited[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0 # cnt 초기화

    print(f'#{test_case} {start} {max_cnt + 1}')
