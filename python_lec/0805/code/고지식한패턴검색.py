p = 'TTA'
t = 'TTTTTABC'
N = len(t)
M = len(p)

cnt = 0
for i in range(N-M+1):  # 비교 시작위치
    for j in range(M):
        if t[i + j] != p[j]:
            break       # for j(어느 반복문을 나가는 break인지 써주면 좋음), 다음 글자부터 비교 시작
    else:               # for j가 중단없이 반복되면
        cnt += 1        # 패턴 개수 1 증가

print(cnt)