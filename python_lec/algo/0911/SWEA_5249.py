from heapq import heappush, heappop

def prim(start):
    heap = []
    MST = [0] * (V+1)
    sum_w = 0

    heappush(heap, (0, start))

    while heap:
        w, v = heappop(heap)

        if MST[v]:
            continue

        MST[v] = 1
        sum_w += w

        for next in range(len(graph[v])):
            # 이미 방문한 지점이면 continue
            if MST[graph[v][next][0]]:
                continue

            heappush(heap, (graph[v][next][1], graph[v][next][0]))

    return sum_w

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]    # 인접리스트
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append([n2, w])
        graph[n2].append([n1, w])

    print(f'#{test_case} {prim(0)}')