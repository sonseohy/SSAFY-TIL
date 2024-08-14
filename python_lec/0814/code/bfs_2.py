def bfs(s):
    queue = []
    visited = [0] * (V+1)

    queue.append(s)
    visited[s] = 1

    while queue:
        v = queue.pop(0)
        print(v)
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True


V, E = map(int, input().split())
arr = list(map(int, input().split()))

graph = [[] for _ in range(V+1)]
for i in range(0, len(arr), 2):
    v1 = arr[i]
    v2 = arr[i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(4)