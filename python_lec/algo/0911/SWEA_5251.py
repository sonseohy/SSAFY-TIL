from heapq import heappush, heappop

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        d, now = heappop(q)

        if distance[now] < d:
            continue

        for next in graph[now]:
            next_node = next[0]
            next_w = next[1]

            new_cost = d + next_w

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heappush(q, (new_cost, next_node))


T = int(input())

for test_case in range(1, T+1):
    N, E = map(int, input().split())
    start = 0
    distance = [1e10] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    dijkstra(start)
    print(f'#{test_case} {distance[N]}')