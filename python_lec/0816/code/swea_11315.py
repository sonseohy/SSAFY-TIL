def game():
    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1]]:
                cnt = 0
                # 4방향의 오목이 되는지 확인
                for k in range(5):
                    ni = i + di * k
                    nj = j + dj * k
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                    else:
                        cnt = 0

                if cnt >= 5:
                    return 'YES'
    return 'NO'

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print(f'#{test_case} {game()}')

# 오답
# cnt = 1로 초기화 하지 않아도 됨