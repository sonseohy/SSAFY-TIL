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
                visited[w] = visited[t] + 1 # 최소 간선을 찾기 때문에 방문 체크와 함께 이동 횟수 저장 (+1)
        # queue가 비었는데 목적지에 도착했을 때
        if queue == [] and visited[g] != 0:
            return visited[g] - 1
    # queue가 비었는데 목적지에 도착하지 못했을 때
    return 0

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[] for _ in range(V+1)]    # 노드가 1번부터 시작하므로 각 노드에 맞는 인덱스에 인접 노드를 저장하기 위해 v+1로 생성 (0번 인덱스는 사용 X)

    # graph에 연결된 노드들을 저장, 방향성이 없으므로 각 노드에 모든 연결된 노드 넣어줘야 함 (graph[a[1]].append(a[0])도 해주는 이유))
    for a in arr:
        graph[a[0]].append(a[1])
        graph[a[1]].append(a[0])    # ex. 1 4 이면 1번 노드 리스트에도 4를 저장, 4번 노드 리스트에도 1을 저장

    print(f'#{test_case} {bfs(S, G, V)}')

'''
def bfs(s, g, v):
    visited = [0] * (v+1)
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.pop(0)

        if t == g:
            return visited[t] - 1

        for w in graph[t]:
            if visited[w] == 0:
                queue.append(w)
                cnt += 1
                visited[w] = visited[t] + 1

    if visited[g] == 0:
        return 0

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    NODE = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for node in NODE:
        v1 = node[0]
        v2 = node[1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(f'#{test_case} {bfs(S, G, V)}')

'''