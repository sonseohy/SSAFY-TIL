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

# 주어진 영역 중 높이의 최댓값 구하기
max_h = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] > max_h:
            max_h = arr[r][c]

result = 0
for h in range(1, max_h+1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for sti in range(N):
        for stj in range(N):
            if arr[sti][stj] > h and visited[sti][stj] == 0:
                safe(sti, stj, h)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)



