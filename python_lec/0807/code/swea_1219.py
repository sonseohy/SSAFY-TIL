def dfs(s):
    visited = [False] * (100)
    stack = []
    stack.append(s)

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for w in graph[v]:
                if not visited[w]:
                    stack.append(w)
        if visited[B] == 1:
            return 1
    return 0


for tc in range(1, 2):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]

    for a in range(0, len(arr), 2):
        graph[arr[a]].append(arr[a+1])

    A = 0
    B = 99

    print(f'#{tc} {dfs(A)}')


# T = int(input())
#
# for test_case in range(1, T + 1):
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V + 1)]
#
#     for _ in range(E):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#
#     S, G = map(int, input().split())
#
#     print(f'#{test_case} {dfs(S)}')