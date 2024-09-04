def recur(row, col, sum_v):
    global result
    if row == N - 1 and col == N - 1:
        if sum_v < result:
            result = sum_v
        return

    if sum_v > result:
        return

    if row + 1 < N:
        recur(row + 1, col, sum_v + CAVES[row + 1][col])

    if col + 1 < N:
        recur(row, col + 1, sum_v + CAVES[row][col + 1])

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    CAVES = [list(map(int, input().split())) for _ in range(N)]
    
    result = 125*125*10
    recur(0, 0, CAVES[0][0])
    print(f'Problem {tc}: {result}')