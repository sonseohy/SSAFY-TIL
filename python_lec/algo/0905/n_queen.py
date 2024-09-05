def check(row, col):
    # 현재 열에 퀸이 있는지 확인
    for i in range(row):
        if visited[i][col] == 1:
            return False    # 한번이라도 체크 되어 있으면 False 반환

    # 왼쪽 대각선 확인
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 오른쪽 대각선 확인
    i, j = row - 1, col + 1
    while i>= 0 and j < N:
        if visited[i][j] == 1:
            return False
        i -= 1
        j += 1

    # # zip 활용 : 코딩테스트에서 주의 (가독성은 좋음)
    # # 왼쪽 대각선 확인 : zip 활용 (but. zip 생각보다 많이 느림)
    # for i, j in zip(range(row-1, -1, -1), range(col-1,-1,-1)):
    #     if visited[i][j] == 1:
    #         return False
    # # 오른쪽 대각선 확인
    # for i, j in zip(range(row-1, -1, -1), range(col+1,N)):
    #     if visited[i][j] == 1:
    #         return False
    #
    # return True

def dfs(row):
    global cnt

    if row == N:    # 퀸들을 리프노드까지 모두 배치한 경우우
       cnt += 1
       return

    for col in range(N):
        if check(row, col): # 유망한가?
            visited[row][col] = 1   # 방문 처리
            dfs(row + 1)    # 다음 행
            visited[row][col] = 0   # Backtracking


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    dfs(0)
    print(f'#{tc} {cnt}')