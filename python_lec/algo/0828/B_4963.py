# 땅 : 1, 바다 : 0
def bfs(i, j):
    global visited

    queue = []
    queue.append([i, j])
    visited[i][j] = True

    while queue:
        ti, tj = queue.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == False and arr[ni][nj] == 1:
                queue.append([ni, nj])
                visited[ni][nj] = True
while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]

    cnt = 0
    visited = [[False] * (W + 1) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                cnt += 1
    print(cnt)