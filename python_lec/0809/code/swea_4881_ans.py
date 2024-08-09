def permu(k, midS):
    global minV

    # 가지치기
    if midS > minV:
        return

    if k == N:
        # sumV = 0
        # for row in range(N):
        #     col = c[row]
        #     sumV += arr[row][col]
        # if sumV < minV:
        #     minV = sumV
        if minV > midS:
            minV = midS
        return

    for i in range(N):
        if not used[i]:
            c[k] = i
            used[i] = True
            permu(k+1, midS + arr[k][i])
            used[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = N * 10

    c = [-1] * N
    used = [False] * N
    permu(0, 0)

    print(f'#{tc} {minV}')

'''
def permu(k):
    global minV
    if k == N:
        sumV = 0
        for row in range(N):
            col = c[row]
            sumV += arr[row][col]
        if sumV < minV:
            minV = sumV

        return

    for i in range(N):
        if not used[i]:
            c[k] = i
            used[i] = True
            permu(k+1)
            used[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = N * 10

    c = [-1] * N
    used = [False] * N
    permu(0)

    print(f'#{tc} {minV}')
'''