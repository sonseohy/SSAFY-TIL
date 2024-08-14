def bfs(i, j):
    visited = [[0]*16 for _ in range(16)]
    queue = []
    queue.append([i,j])
    visited[i][j] = 1

    while queue:
        ti, tj = queue.pop(0)

        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            wi, wj = ti+di, tj+dj
            if 0 <= wi < 16 and 0 <= wj < 16 and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                queue.append([wi, wj])
                visited[wi][wj] = 1
    return 0

T = 1

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    start_i = start_j = 1

    print(f'#{test_case} {bfs(start_i, start_j)}')


