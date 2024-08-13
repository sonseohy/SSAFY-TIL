import copy
def paint(blue):
    tmp = copy.deepcopy(arr)
    min_cnt = 0
    for i in range(1, N-1):
        for j in range(M):
            if i == blue:
                if tmp[i][j] != 'B':
                    min_cnt += 1
            elif i < blue:
                if tmp[i][j] != 'W':
                    min_cnt += 1
            elif i > blue:
                if tmp[i][j] != 'R':
                    min_cnt += 1
    return min_cnt


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    result = 2501
    for i in range(N):
        for j in range(M):
            if i == 0:
                if arr[i][j] != 'W':
                    cnt += 1
            elif i == N-1:
                if arr[i][j] != 'R':
                    cnt += 1
            else:
                blue = i
                min_paint = paint(blue)
                if min_paint < result:
                    result = min_paint
                break
    cnt += result
    print(f'#{test_case} {cnt}')