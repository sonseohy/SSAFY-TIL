# 인접 조건 1. 벽이 아니고 2. 방문한 적이 없는 칸이 최종적으로 인큐할 대상
def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)] # visited 생성
    queue = []          # 큐 생성
    queue.append([i, j]) # 시작점 인큐
    visited[i][j] = 1   # 시작점 인큐 표시
    # 탐색
    while queue:
        ti, tj = queue.pop(0)
        if maze[ti][tj] == 3:
            return visited[ti][tj] - 1 - 1 # 경로의 빈칸 수, -1 (visited - 1은 최단경로 수)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # 미로 내부이고, 인접이고 벽이 아니면
            wi, wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                # 인큐
                queue.append([wi, wj])
                # 인큐 표시
                visited[wi][wj] = visited[ti][tj] + 1
    return 0 # 3에 도달하지 못하면


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)


    print(f'#{test_case} {bfs(sti, stj, N)}')