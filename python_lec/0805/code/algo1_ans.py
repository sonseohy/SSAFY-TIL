# 풍선팡 2
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = -100 * 5

    for row in range(N):
        for col in range(N):
            sumV = arr[row][col] # 내 위치의 값도 더해야하므로
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 방향 상관없이 상하좌우 값을 더할 경우 이런식으로 작성 가능
                newR = row + dr
                newC = col + dc
                if 0 <= newR < N and 0 <= newC < N:
                    sumV += arr[newR][newC]
            if maxV < sumV:
                maxV = sumV

    print(f'#{test_case} {maxV}')

# 풍선팡
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = -100 * 5

    for row in range(N):
        for col in range(N):
            sumV = arr[row][col] # 내 위치의 값도 더해야하므로
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 방향 상관없이 상하좌우 값을 더할 경우 이런식으로 작성 가능
                k = 4 # ? k위치 확실하지 않음
                for i in range(1, k):
                    newR = row + dr + k
                    newC = col + dc + k
                    if 0 <= newR < N and 0 <= newC < N:
                        sumV += arr[newR][newC]
            if maxV < sumV:
                maxV = sumV

    print(f'#{test_case} {maxV}')
