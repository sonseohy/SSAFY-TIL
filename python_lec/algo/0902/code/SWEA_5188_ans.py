def recur(row, col, mid_sum):
    global result
    if row == N - 1 and col == N - 1:
        if mid_sum < result:
            result = mid_sum
        return

    if mid_sum > result:
        return

    if row + 1 < N:
        recur(row + 1, col, mid_sum + arr[row + 1][col])

    if col + 1 < N:
        recur(row, col + 1, mid_sum + arr[row][col + 1])


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    row = col = 0
    result = 10e8
    recur(row, col, arr[0][0])
    print(f'#{test_case} {result}')


# def recur(row, col, lst, mid_sum):
#     global result
#     if row == N-1 and col == N-1:   # 기저조건
#         print(mid_sum, lst)
#         if mid_sum < result:
#             result = mid_sum
#         return
#
#     if row+1 < N:
#         recur(row+1, col, lst+[(row+1, col)], mid_sum+arr[row+1][col])
#
#     if col+1 < N:
#         recur(row, col+1, lst+[(row, col+1)], mid_sum+arr[row][col+1])
#
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     row = col = 0
#     result = 300
#     recur(row, col, [(0, 0)], arr[0][0])
#     print(f'#{test_case} {result}')
