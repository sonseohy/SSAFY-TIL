# 재귀 : 시간초과
def recur(r, c, s):
    global result, visited
    visited[r][c] = True
    if r == N-1 and c == N-1:
        if s < result:
            result = s
        return
    if s > result:
        return

    if r + 1 < N and visited[r+1][c] == False:
        recur(r+1, c, s+CAVES[r+1][c])
        visited[r+1][c] = False

    if c + 1 < N and visited[r][c+1] == False:
        recur(r, c+1, s+CAVES[r][c+1])
        visited[r][c+1] = False

    if r - 1 >= 0 and visited[r-1][c] == False:
        recur(r - 1, c, s + CAVES[r - 1][c])
        visited[r-1][c] = False

    if c - 1 >= 0 and visited[r][c-1] == False:
        recur(r, c-1, s+CAVES[r][c-1])
        visited[r][c-1] = False

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    CAVES = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')

    visited = [[False]*N for _ in range(N)]

    recur(0, 0, CAVES[0][0])
    print(f'Problem {tc}: {result}')

# # 시도 2 재귀 실패(위로 가는 경우도 있음)
# def recur(r, c, s):
#     global result
#     if r == N-1 and c == N-1:
#         if s < result:
#             result = s
#             print(result)
#         return
#     if s > result:
#         return

#     if r + 1 < N:
#         recur(r+1, c, s+CAVES[r+1][c])

#     if c + 1 < N:
#         recur(r, c+1, s+CAVES[r][c+1])

# tc = 0
# while True:
#     tc += 1
#     N = int(input())
#     if N == 0:
#         break
#     CAVES = [list(map(int, input().split())) for _ in range(N)]

#     result = 125*125*9+1
#     recur(0, 0, CAVES[0][0])
#     print(f'Problem {tc}: {result}')

# 시도 1 : bfs 실패
# def solve(i, j):
#     global visited
#     visited[i][j] = True
#     sum_v = CAVES[i][j]
#     min_v = 10
#
#     queue = []
#     queue.append([i,j])
#
#     while queue:
#         ti, tj = queue.pop(0)
#
#         for di, dj in [[0, 1], [1, 0]]:
#             ni, nj = ti + di, tj + dj
#             if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:
#                 queue.append([ni, nj])
#                 visited[ni][nj] = True
#                 print(ni,nj)
#                 sum_v += CAVES[ni][nj]
#
#     return sum_v
#
# tc = 0
# while True:
#     tc += 1
#     N = int(input())
#     if N == 0:
#         break
#     CAVES = [list(map(int, input().split())) for _ in range(N)]
#
#     visited = [[False] * N for _ in range(N)]
#     total_sum = solve(0, 0)
#     print(f'Problem {tc}: {total_sum}')