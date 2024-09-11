T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[1e10]* N for _ in range(N)]
    D[0][0] = 0

    Q = [(0, 0)]
    while Q:
        row, col = Q.pop(0)
        for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < N:
                value = max(arr[nr][nc] - arr[row][col], 0)+1
                if D[nr][nc] > D[row][col] + value:
                    D[nr][nc] = D[row][col] + value
                    Q.append((nr, nc))

    print(D[N-1][N-1])