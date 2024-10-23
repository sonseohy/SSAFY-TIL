# def dfs(row, col, current_sum, visited, result):
#     # 도착점에 도달했을 때
#     if row == N-1 and col == N-1:
#         if current_sum < result[0]:
#             result[0] = current_sum
#         return
    
#     # 현재 경로의 합이 현재 최솟값보다 크면 종료
#     if current_sum >= result[0]:
#         return
    
#     # 네 방향으로 이동
#     for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#         nr, nc = row + dr, col + dc
#         if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#             visited[nr][nc] = True
#             dfs(nr, nc, current_sum + CAVES[nr][nc], visited, result)
#             visited[nr][nc] = False  # 되돌리기
            
# # 초기화 및 호출 예시
# tc = 0
# while True:
#     tc += 1
#     N = int(input())
#     if N == 0:
#         break
#     CAVES = [list(map(int, input().split())) for _ in range(N)]

#     visited = [[False] * N for _ in range(N)]
#     result = [float('inf')]
#     visited[0][0] = True
#     dfs(0, 0, CAVES[0][0], visited, result)
#     print(f'Problem {tc}: ',*result)

# gpt - dfs 재귀
def dfs(row, col, current_sum):
    global result
    
    # 도착점에 도달했을 때
    if row == N-1 and col == N-1:
        result = min(result, current_sum)
        return
    
    # 현재 경로의 합이 현재 최솟값보다 크면 종료
    if current_sum >= result:
        return
    
    # 네 방향으로 이동
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, current_sum + CAVES[nr][nc])
            visited[nr][nc] = False  # 되돌리기

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    CAVES = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    dfs(0, 0, CAVES[0][0])
    print(f'Problem {tc}: {result}')


# 내코드
def dfs(row, col):
    global result

    stack = [(row, col, CAVES[row][col])]  # (row, col, current_sum)
    visited = [[False]*N for _ in range(N)]
    visited[row][col] = True

    while stack:
        r, c, s = stack.pop()
        min_v = 10
        # If we reached the bottom-right corner
        if r == N-1 and c == N-1:
            if s < result:
                result = s
            continue

        # If current path exceeds the known result, no need to proceed
        if s >= result:
            continue


        # Check the four possible moves and push them to the stack if valid
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False and min_v > CAVES[nr][nc]:
                min_v = CAVES[nr][nc]
                visited[nr][nc] = True
                stack.append((nr, nc, s + CAVES[nr][nc]))

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    CAVES = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    dfs(0, 0)
    print(f'Problem {tc}: {result}')

# for i in range(5):
#     print('손서현 바보')