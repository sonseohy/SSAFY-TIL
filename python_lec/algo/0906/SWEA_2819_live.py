import sys
sys.stdin = open('input.txt', 'r')

# 시작점 : 각 좌표
# 끝 점 : 문자열의 길이가 7이면 종료
def dfs(i, j, path):
    if len(path) == 7:
        result.add(path)    # 현재까지의 경로를 결과 set에 저장
        return
    # 상하좌우 확인하면서 갈 수 있으면 이동
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        # 범위 체크
        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
            continue

        dfs(ni, nj, path+arr[ni][nj])   # 문자열을 누적하면서 다음으로 이동

T = int(input())

for tc in range(1, T+1):
    # 문자로 쓰면 합치기 더 쉽기 때문에, 각 칸을 문자로 입력받음
    arr = [input().split() for _ in range(4)]
    # 중복을 제거하기 위해
    result = set()

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 모든 지점을 확인
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j]) # 칸을 이동할 때 필요한 정보들 1. 좌표, 2. 누적된 문자열

    print(f'#{tc} {len(result)}')