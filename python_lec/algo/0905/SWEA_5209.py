def min_cost(product, sum_cost):
    global total_sum
    if product == N:
        if total_sum > sum_cost:    # 오답 : total_sum을 무조건 sum_cost로 바꾸는 것이 아니라 sum_cost가 total보다 작은 경우에 total을 갱신해야함 -> 그래야 최소 합이 나옴
            total_sum = sum_cost
        return

    if sum_cost >= total_sum:   # sum_cost와 total_sum이 같아도 굳이 밑을 보지 않아도 됨
        return

    for i in range(N):
        if used[i] == 1:
            continue
        sum_cost += COSTS[product][i]
        used[i] = 1
        min_cost(product+1, sum_cost)
        sum_cost -= COSTS[product][i]
        used[i] = 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    COSTS = [list(map(int, input().split())) for _ in range(N)]

    total_sum = float('inf')
    used = [0] * N  # 방문한 공장 체크
    min_cost(0, 0)
    print(f'#{test_case} {total_sum}')