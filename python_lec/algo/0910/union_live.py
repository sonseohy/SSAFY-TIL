def make_set(n):
    p = [i for i in range(n)]   # 각 원소의 부모를 자신으로 초기화
    return p

def find(x):
    if parents[x] == x: # x 자기자신이 x를 바라본다 == 해당 집합의 대표자를 찾았다
        return x

    # x의 부모가 가리키고 있는 정점부터 다시 대표자를 탐색
    return find(parents[x])

    # # 경로압축
    # parents[x] = find(parents[x])
    # return parents[x]

def union(x, y):
    # x와 Y의 대표자를 찾자
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:    # 이미 같은 집합이면 끝
        return

    # 다른 집합이라면 더 작은 루트노드에 합친다
    # 문제에 따라 다르지만 우선은 더 작은 노드로 합침
    if root_x < root_y:
        parents[y] = root_x # y가 바라보는 부모는 x의 대표자
    else:
        parents[x] = root_y

n = 7   # 원소의 개수
parents = make_set(n)   # 집합생성. parents에 부모 정보들을 저장

union(1, 3)
union(2, 3)
union(5, 6)

print(parents)  # 대표자의 수 == 집합의 수