# bfs를 이용해 비에 잠기지 않은 구역을 방문 표시
def safe(i, j, h):
    global visited
    queue = []
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        ti, tj = queue.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] > h:
                queue.append([ni, nj])
                visited[ni][nj] = 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 주어진 영역 중 높이의 최댓값 구하기 (모두 잠긴 이후에는 계산하지 않아도 되므로)
max_h = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] > max_h:
            max_h = arr[r][c]

result = 0
# max_h 높이까지 arr 탐색을 해야하므로 max_h +1까지 높이를 반복
for h in range(max_h+1):    # 오답 : 비가 오지 않을 때도 체크해야하므로 1부터가 아닌 0부터
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for sti in range(N):
        for stj in range(N):
            if arr[sti][stj] > h and visited[sti][stj] == 0:    # h보다 커서 잠기지 않았고, 방문하지 않은 곳에 대해 bfs 진행
                safe(sti, stj, h)
                cnt += 1    # 잠기지 않은 한구역을 모두 방문 했을 때 cnt += 1

    if result < cnt:    # 최대 영역 개수 계산
        result = cnt

print(result)



