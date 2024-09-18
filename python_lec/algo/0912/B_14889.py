# 능력치 차이 구하기
def power(start):
    global result
    start_p = link_p = 0
    link = set(person) - start  # 전체 인원 중 스타트 팀원에 속하지 않은 사람을 링크 팀으로

    for i in start:     # 스타트 팀의 능력치 계산
        for j in start:
            if i != j:
                start_p += S[i-1][j-1]

    for r in link:      # 링크 팀의 능력치 계산
        for c in link:
            if r != c:
                link_p += S[r-1][c-1]

    result = min(result, abs(start_p-link_p))   # 능력치 차이의 최솟값 갱신

# 조합을 이용해 팀원 나누기
def team(n, start):
    if n == N / 2:
        power(group)
        return

    for i in range(start, N):
        group.add(person[i])
        team(n+1, i+1)
        group.remove(person[i])

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

person = list(range(1, N+1))
group = set()
result = 1e5
team(0, 1)

print(result)