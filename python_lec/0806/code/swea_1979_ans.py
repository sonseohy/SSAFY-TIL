def get_onerow(row):
    cnt = 0
    total = 0
    for col in range(N):
        if arr[row][col] == 1:
            cnt += 1
        else:
            if cnt == K:
                total += 1
            cnt = 0
    if cnt == K:
        total += 1
    return total

def get_onecol(col):
    cnt = 0
    total = 0
    for row in range(N):
        if arr[row][col] == 1:
            cnt += 1
        else:
            if cnt == K:
                total += 1
            cnt = 0
    if cnt == K:
        total += 1
    return total

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for row in range(N):
        result += get_onerow(row)

    for col in range(N):
        result += get_onecol(col)

    print(f'#{tc} {result}')