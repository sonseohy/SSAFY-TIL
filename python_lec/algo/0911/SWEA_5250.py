from heapq import heappush, heappop

def dijkstra(i, j):
    q = []
    heappush(q, (0, i, j))
    distance[i][j] = 0

    while q:
        d, now_i, now_j = heappop(q)

        if distance[now_i][now_j] < d:
            continue

        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni = now_i + di
            nj = now_j + dj
            if 0 <= ni < N and 0 <= nj < N:
                next_i = ni
                next_j = nj

                # new_w : 높이가 같으면 1, 높이가 크면 차이만큼 추가 연료 소비
                new_w = 1
                if height[next_i][next_j] > height[now_i][now_j]:
                    new_w += height[next_i][next_j] - height[now_i][now_j]
                new_cost = d + new_w

                if new_cost >= distance[next_i][next_j]:
                    continue

                distance[next_i][next_j] = new_cost
                heappush(q, (new_cost, next_i, next_j))

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]

    sti = stj = 0
    distance = [[1e9]*N for _ in range(N)]
    dijkstra(sti, stj)

    print(f'#{test_case} {distance[N-1][N-1]}')