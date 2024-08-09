# v에서 goal(3)까지 갈 수 있으면 1, 없으면 0을 return
def dfs_r(vr, vc):
    if arr[vr][vc] == 3:
        return 1
    visited[vr][vc] = True

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        wr = vr + dr
        wc = vc + dc
        if 0 <= wr < N and 0 <= wc < N and arr[wr][wc] != 1 and not visited[wr][wc]:
            if dfs_r(wr, wc) == 1:
                return 1
    return 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]  # .strip()으로 공백이 붙어서 입력이 들어오는 경우 방지

    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                stR = row
                stC = col
                break

    visited = [[False] * N for _ in range(N)]
    print(f'#{tc} {dfs_r(stR, stC)}')