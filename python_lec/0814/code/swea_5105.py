def bfs(i, j, n):
    visited = [[0] * n for _ in range(n)]
    queue = []
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        ti, tj = queue.pop(0)

        if maze[ti][tj] == 3:
            return visited[ti][tj] -1 -1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            wi, wj = ti+di, tj+dj
            if 0 <= wi < n and 0 <= wj < n and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                queue.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
    return 0

def start_point(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    start_i, start_j = start_point(N)

    print(f'#{test_case} {bfs(start_i, start_j, N)}')
