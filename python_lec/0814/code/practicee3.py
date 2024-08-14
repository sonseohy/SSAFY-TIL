'''
7 8 # 마지막 정점 번호, 간선 수
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(s, V):  # 시작점 s, 마지막 정점 V
    # 준비 : visited 생성, 큐 생성, 시작점 enqueue, 시작점 방문(인큐됨) 표시
    visited = [0] * (V + 1)
    queue = []
    queue.append(s)
    visited[s] = 1

    # 탐색
    while queue:    # 큐가 비어있지 않으면 == 탐색할 정점이 남아있으면 (front와 rear가 다르면)
        # t <- 디큐
        t = queue.pop(0)
        # 처리
        print(t)
        # t에 인접이고, 인큐된 적이 없으면 인큐하고 인큐됨 표시
        for w in adj_l[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1  # visited[w] = visited[t] + 1 (최단거리, 최단시간을 구할 때)

V, E = map(int, input().split())    # V : 마지막 정점 번호, E : 간선 수
arr = list(map(int, input().split()))

adj_l = [[] for _ in range(V + 1)]  # 인접 리스트 생성 (0번 정점은 없으므로 V + 1)
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2 + 1] # 한 쌍 씩 읽어옴 (1,2), (1,3) ...
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우

bfs(1, V) # 출발점, 정점수