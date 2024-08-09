# 스택에 넣으면서 방문 체크
def dfs(s):
    stack = []
    visited = [False] * (N + 1)
    stack.append(s) # while문이 안돌아가기 때문
    visited[s] = True

    while stack:
        v = stack.pop()
        print(v)
        for w in graph[v]:
            if not visited[w]:
                stack.append(v)
                visited[w] = True


'''
# 스택에 첫 노드를 넣어준 후 해당 노드를 pop 하면서 pop한 노드의 자식 노드들을 push
# 가장 끝의 노드를 팝하면서 또 자식 노드를 push
# 해당 과정을 반복하면서 방문 표시하는 반복으로 탐색

def dfs(s):
    stack = []
    visited = [False] * (N + 1)
    stack.append(s) # while문이 안돌아가기 때문
    
    while stack:
        v = stack.pop()
        if not visited[v]:      # 방문하지 않은 경우에만
            visited[v] = True   # 방문한 v는 표시
            for w in graph[v]:
                if not visited[w]:  # 방문 표시가 없는 w만 스택에 push, But. pop이 안된 상태이면 방문 체크가 안되었으므로 스택에 중복 값 생성될 수 있음
                    stack.append(w)
'''
N = 7   # vertex로 1 ~ 7까지 사용

graph = [[] for _ in range(N + 1)]  # 빈 그래프 생성

s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
numbers = list(map(int, input().split()))

# 인접 리스트로 그래프 생성
for i in range(0, len(numbers), 2):
    v1 = numbers[i]
    v2 = numbers[i + 1]

    graph[v1].append(v2)
    graph[v2].append(v1)

# # 인접 행렬로 그래프 생성
# graph = [[0] * (N + 1) for _ in range(N+1)]
#
# for i in range(0, len(numbers), 2):
#     v1 = numbers[i]
#     v2 = numbers[i + 1]
#
#     graph[v1][v2] = 1
#     graph[v2][v1] = 1


'''
graph = [[], [2, 3], [1, 4, 5], [1, 7], ...] # 인접 리스트 방식으로 그래프 생성하는 방법
# 인접 행렬 방식으로 그래프 생성하는 방법
graph = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],   # 1과 연결된 노드의 숫자에 1
    [0, 1, 0, 0, 1, 1, 0, 0],   # 2와 연결된 노드의 숫자에 1 (인덱스 1, 4, 5에 1)
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
'''

# 재귀
visited = [False] * (N+1)
def dfs_r(v):
    print(v)
    visited[v] = True

    for w in graph[v]:
        if not visited[w]:
            dfs_r(w)

dfs_r(1)

'''
# 인접 행렬 dfs
# 순서가 dfs와 동일하게 나오진 않음
def dfs(s):
    visited = [False] * (N+1)
    stack = []
    stack.append(s)
    visited[s] = True

    while stack:
        v = stack.pop()
        print(v)

        for w in range(N+1):
            if graph[v][w] == 0:
                continue
            if not visited[w]:
                stack.append(w)
                visited[w] = True
'''