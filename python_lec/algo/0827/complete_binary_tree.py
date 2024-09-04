'''
# tc1
15
ABCDE
# tc2
6
ABCDE
'''

def preorder(root_idx):
    # # ver1
    # print(TREE[root_idx])
    # if root_idx * 2 <= N:
    #     preorder(root_idx * 2)  # left
    # if root_idx * 2 + 1 <= N:
    #     preorder(root_idx * 2 + 1)  # right

    # if root_idx <= N: # tc2 일 때 유리 (TREE 공간이 딱 맞을 때)
    if TREE[root_idx]:  # tc1 일 때 유리 (TREE 공간이 넉넉할 때)
        print(TREE[root_idx])
        preorder(root_idx * 2)  # left
        preorder(root_idx * 2 + 1)  # right

def inorder(root_idx):
    if root_idx <= N:
        preorder(root_idx * 2)  # left
        print(TREE[root_idx])
        preorder(root_idx * 2 + 1)  # right

def postorder(root_idx):
    if root_idx <= N:
        preorder(root_idx * 2)  # left
        preorder(root_idx * 2 + 1)  # right
        print(TREE[root_idx])

N = int(input())
arr = input()

TREE = [0]*(N+1)
for i in range(len(arr)):
    TREE[i+1] = arr[i]

print(TREE)
preorder(1) # root index를 보내줘야함