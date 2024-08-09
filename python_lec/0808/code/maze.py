# 3인 곳에 도달할 수 있으면 1을, 아니면 0을 return
def dfs(stR, stC):
    stack = []
    visited = [[False] * N for _ in range(N)]
    stack.append((stR, stC))
    visited[stR][stC] = True

    while stack:
        vr, vc = stack.pop()
        if arr[vr][vc] == 3:
            return 1

        for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            wr = vr + dr
            wc = vr + dc
            if 0 <= wr < N and 0 <= wc < N:
                if not visited[wr][wc] and arr[wr][wc] != 1: # (arr[wr][wc] == 0 or arr[wr][wc] == 3)
                    stack.append((wr, wc))
                    visited[wr][wc] = True

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)] # .strip()으로 공백이 붙어서 입력이 들어오는 경우 방지

    # 1. 시작지점 먼저 찾기
    '''
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                stR = row
                stC = col
                break
    '''
    for row in range(N):
        if arr[row].count(2):   # 리스트에서 2의 개수가 0개 이상이면
            stR = row
            stC = arr[row].index(2)
            break

    print(f'#{tc} {dfs(stR, stC)}')
