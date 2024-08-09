def dfs(s):
    visited = [False] * (V+1)
    stack = []
    stack.append(s)

    while stack:
        v = stack.pop()
        print(v)
        if not visited[v]:
            visited[v] = True
            for w in graph[v]:
                if not visited[w]:
                    stack.append(w)
        print(visited)
        if visited[G] == 1:
            return 1
    return 0


T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    S, G = map(int, input().split())

    print(f'#{test_case} {dfs(S)}')


'''
T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)] # 입력이 들어온대로 저장하면 됨, 굳이 리스트로 받아서 풀 필요 X
    S, G = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for a in arr:
        v1 = a[0]
        v2 = a[1]

        graph[v1].append(v2)
        graph[v2].append(v1)
    print(graph)
    print(f'#{test_case} {dfs(S)}')
'''

'''
T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1) # 문제에서 방향성 그래프라고 했으므로, 시작 지점에서 자식 노드만 봤을 때 경로를 봐야함
    S, G = map(int, input().split())

    print(f'#{test_case} {dfs(S)}')
'''

