def bfs(s, g, v):
    visited = [0] * (v + 1)
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.pop(0)

        for w in graph[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1

        if queue == [] and visited[g] != 0:
            return visited[g] - 1

    return 0

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    cnt = 0
    for a in arr:
        graph[a[0]].append(a[1])
        graph[a[1]].append(a[0])

    print(f'#{test_case} {bfs(S, G, V)}')