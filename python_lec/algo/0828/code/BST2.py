def find(key):
    pos = 1
    while TREE[pos] != -1:
        if TREE[pos] == key:
            return pos
        if TREE[pos] < key:
            pos = pos*2 + 1
        else:
            pos = pos*2
    return -1

def insert(key):
    pos = 1
    while TREE[pos] != -1:
        if TREE[pos] == key:
            return 'input error'    # 이미 트리에 같은 값이 있으면 error 출력
        if TREE[pos] < key:
            pos = pos*2 + 1
        else:
            pos = pos*2
    TREE[pos] = key

# TREE = [-1, 9, 4, 12, 3, 6, -1, 15, -1, -1, -1, -1, -1, -1, 13, 17] + [-1] * 100    # -1에는 데이터 들어있지 않다고 가
# print(find(13))
# print(find(9))
# print(find(17))
# print(find(14))
#
# insert(14)
# print(TREE)
# insert(5)
# print(TREE)

TREE = [-1] * 100
# arr = [9, 4, 12, 3, 6, 15, 13, 17]
arr = [4, 6, 7, 8]
for d in arr:
    insert(d)
    print(TREE)