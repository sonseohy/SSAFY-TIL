N = int(input())

arr = [[0] * N for _ in range(N)]
arr[0][0] = 1
for row in range(1, N):
    arr[row][0] = 1
    arr[row][row] = 1
    for col in range(1, row+1):
        arr[row][col] = arr[row-1][col] + arr[row-1][col-1]

for i in range(N):
    print(*arr[i][:i+1])