'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# tree(root)를 입력 받아 root - 왼쪽 - 오른쪽 자식 노드의 순으로 순회
def preorder(root): # 인수로 시작 정점 받음
    print(root)
    for c in TREE[root]:
        preorder(c)

    # # 코드 2
    # print(root)
    # if len(TREE[root]) >= 1:
    #     inorder(TREE[root][0])
    # if len(TREE[root]) == 2:
    #     inorder(TREE[root][1])

# tree(root)를 입력 받아 왼쪽 - root - 오른쪽 자식 노드의 순으로 순회
def inorder(root):
    if len(TREE[root]) >= 1:
        inorder(TREE[root][0])
    print(root)
    if len(TREE[root]) == 2:
        inorder(TREE[root][1])

# tree(root)를 입력 받아 왼쪽 - 오른쪽 - root 자식 노드의 순으로 순회
def postorder(root):
    if len(TREE[root]) >= 1:
        postorder(TREE[root][0])
    if len(TREE[root]) == 2:
        postorder(TREE[root][1])
    print(root)

N = int(input())
arr = list(map(int, input().split()))

TREE = [[] for _ in range(N+1)]
for i in range(0, len(arr), 2):
    p = arr[i]
    c = arr[i+1]

    TREE[p].append(c)

print(TREE)

# preorder(3)
# preorder(1)
# inorder(1)
postorder(1)