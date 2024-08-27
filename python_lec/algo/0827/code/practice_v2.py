# 호출 횟수는 적으나 if문이 많아 시간이 걸릴 수 있음
def preorder1(root):
    print(root)
    if TREE[root][0]:
        preorder(TREE[root][0])
    if TREE[root][1]:
        preorder(TREE[root][1])

# 호출 횟수는 많으나 if문이 적어 시간이 적게 들 수 있음
def preorder(root):
    # if root == 0:
    #     return
    if root:
        print(root)
        preorder(TREE[root][0])
        preorder(TREE[root][1])

def inorder(root):
    if root:
        preorder(TREE[root][0])
        print(root)
        preorder(TREE[root][1])

def postorder(root):
    if root:
        preorder(TREE[root][0])
        preorder(TREE[root][1])
        print(root)

N = int(input())
arr = list(map(int, input().split()))

TREE = [[0, 0] for _ in range(N+1)]
for i in range(0, len(arr), 2):
    p = arr[i]
    c = arr[i+1]

    if TREE[p][0] == 0:
        TREE[p][0] = c
    else:
        TREE[p][1] = c

print(TREE)

preorder(1)
inorder(1)
postorder(1)