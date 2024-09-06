# 시작점 : 0번 점원 / 탑의 높이는 0부터 시작
# 끝점 (기저조건) : N명의 점원을 탑에 쌓을지 말지 고려를 완료

import sys
sys.stdin = open('input.txt', 'r')

def recur(cnt, sum_height):
    global ans

    # 기저조건 : 가지치기 : 이미 탑의 높이가 B 이상이라면, 더 이상 확인할 필요가 X
    # 가지치기를 기저조건 밑에 넣을지 위에 넣을지 순서에 따라 ans가 체크 되므로 순서 중요
    if sum_height >= B:
        # B 이상인 탑 중 가장 낮은 것이 정답
        ans = min(ans, sum_height)
        return

    if cnt == N:    # 기저조건 : 모든 점원을 탑을 쌓는데 고려했는가?
        return

    # cnt번 점원을 탑에 쌓는다
    recur(cnt + 1, sum_height + heights[cnt])
    # 안 쌓는다
    recur(cnt + 1, sum_height)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))   # 각 점원의 키
    ans = 1e9 # 점원들을 쌓은 탑 중 B에 가장 가까운 높이를 저장 (1e9 : 1억)

    recur(0, 0)
    print(f'#{tc} {ans - B}')