row, col = map(int, input().split())
N = int(input())
LINE = [list(map(int, input().split())) for _ in range(N)]

# 가로로 잘라야하는 점선번호와 세로로 잘라야하는 점선을 각각 리스트로 묶음
# 가로 : cut[0], 세로 : cut[1]
# 가로는 세로로 잘리므로 col의 최대 길이 저장, 세로는 가로로 잘리므로 row의 최대 길이 저장
cut = [[0, col], [0, row]]  # 잘라야 하는 범위를 알기 위해 종이의 가로 / 세로 길이를 각각 넣어둠
for k in LINE:
    cut[k[0]].append(k[1])  # k[0] : 자르는 점선이 가로인지 세로인지, k[1] : 점선 번호

# 조각의 최대길이를 찾기 위해 점선 번호를 정렬
cut[0].sort()
cut[1].sort()

# 가로 조각의 최대 길이 찾기
max_r = 0
for r in range(1, len(cut[0])):
    len_r = cut[0][r] - cut[0][r-1]
    if max_r < len_r:
        max_r = len_r

# 세로 조각의 최대 길이 찾기
max_c = 0
for c in range(1, len(cut[1])):
    len_c = cut[1][c] - cut[1][c-1]
    if max_c < len_c:
        max_c = len_c

print(max_r * max_c)