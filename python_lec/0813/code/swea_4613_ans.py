def cal(wb, br):
    sumV = 0
    for i in range(0, wb):
        sumV += counts[i][1] + counts[i][2]
    for i in range(wb, br+1):
        sumV += counts[i][0] + counts[i][2]
    for i in range(br+1, N):
        sumV += counts[i][0] + counts[i][1]

    return sumV

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    counts = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        counts[i][0] = arr[i].count('W')
        counts[i][1] = arr[i].count('B')
        counts[i][2] = arr[i].count('R')

    minV = N * M
    for wb in range(1, N-1):     # white-blue의 경계
        for br in range(wb, N-1):       # blue-red의 경계
            val = cal(wb, br)
            if minV > val:
                minV = val

    print(f'#{tc} {minV}')

'''
def cal(wb, br):
    sumV = 0
    for i in range(0, wb):
        sumV += counts[i][1] + counts[i][2]
    for i in range(wb, br):
        sumV += counts[i][0] + counts[i][2]
    for i in range(br, N):
        sumV += counts[i][0] + counts[i][1]

    return sumV

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    counts = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        counts[i][0] = arr[i].count('W')
        counts[i][1] = arr[i].count('B')
        counts[i][2] = arr[i].count('R')

    minV = N * M
    for wb in range(1, N-1):     # white-blue의 경계
        for br in range(wb+1, N):       # blue-red의 경계
            val = cal(wb, br)
            if minV > val:
                minV = val

    print(f'#{tc} {minV}')
'''