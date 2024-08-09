'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def DFS(s, v):                  # s : 시작정점, v : 정점개수(1번부터 시작인 정점의 마지막 정점)
    visited = [0] * (v + 1)     # 방문한 정점을 표시
    stack = []                  # 스택 생성
    visited[s] = 1              # 시작점 방문 표시
    v = s                       # 현재 정점을 v라고 하고 시작 정점을 현재 정점으로
    while True:
        for w in adjL[v]: # v에 인접하고, 방문하지 않은 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # push(v) 현재 정점을 push하고
                v = w            # w에 방문
                visited[w] = 1   # w에 방문 표시
                break            # v부터 다시 탐색 (갈림길을 선택하기 위해)
        else:                    # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
            if stack:            # 이전 갈림길을 스택에서 꺼내서... if TOP > -1
                v = stack.pop()  # stack에 남은게 있다면 꺼냄
            else:                # stack이 비어있다면 (되돌아갈 곳이 없으면, 남은 갈림길이 없으면 탐색 종료)
                break            # while True

# for else: 중간에 break로 나오지 않았다면 else로 가는 문법
T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    arr = list(map(int, input().split()))
    for i in range(E):  # 2개씩 읽어보는 코드
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1) # 단방향이 아니기 때문에 위의 코드만 작성하면 2가 1과 4와 연결되었지만 1이 빠져 4만 연결되어 있다는 리스트가 생성됨

    DFS(1, V)



'''
adjl[0] : 사용 X
adjl[1] : 1에 인접한 정점
'''