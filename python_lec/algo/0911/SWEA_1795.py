from heapq import heappush, heappop

def dijkstra(start):
    q = []
    heappush(q, (0,  start))
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
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append([y, c])

    go = []
    back = []
    for i in range(1, N+1):
        distance = [1e9] * (N + 1)
        dijkstra(i)
        if i == X:
            go = distance[1:]
        back.append(distance[X])
        print(distance)
    print(go)
    print(back)
    result = []
    for j in range(N):
        result.append(go[j] + back[j])
    print(result)

    print(f'#{test_case} {max(result)}')
# from heapq import heappush, heappop
#
# def dijkstra(start):
#     q = []
#     heappush(q, (0,  start))
#     distance[start] = 0
#
#     while q:
#         d, now = heappop(q)
#
#         if distance[now] < d:
#             continue
#
#         for next in graph[now]:
#             if now == X:
#                 continue
#             next_node = next[0]
#             next_w = next[1]
#
#             new_cost = d + next_w
#
#             if new_cost >= distance[next_node]:
#                 continue
#
#             distance[next_node] = new_cost
#
#             heappush(q, (new_cost, next_node))
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N, M, X = map(int, input().split())
#     graph = [[] for _ in range(N+1)]
#     for _ in range(M):
#         x, y, c = map(int, input().split())
#         graph[x].append([y, c])
#
#     time = [0] * (N+1)
#
#     for i in range(1, N+1):
#         distance = [1e9] * (N + 1)
#         if i == X:
#             continue
#         dijkstra(i)
#         time[i] = distance[2]
#
#
#     print(time)
