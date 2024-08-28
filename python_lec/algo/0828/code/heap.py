def insert(key):
    global last

    last += 1
    TREE[last] = key

    c = last
    p = c//2
    while p >= 1:   # root 값도 비교해야하므로 >=
        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            # else break 안쓰고 밑의 코드로도 가능
            c = p
            p = c//2
        else:
            break

    # # 간단ver
    # while p >= 1 and TREE[p] < TREE[c]:
    #         TREE[p], TREE[c] = TREE[c], TREE[p]
    #         c = p
    #         p = c//2

def dequeue():
    global last
    result = TREE[1]
    TREE[1] = TREE[last]
    last -= 1

    p = 1
    c = p*2
    while c <= last:
        if c < last and TREE[c] < TREE[c+1]: # 먼저 왼쪽, 오른쪽 노드 값 비교
            c = c+1
        if TREE[p] < TREE[c]:   # 무조건 왼쪽 값을 넣어놓음
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p*2
        else:
            break

    return result

TREE = [-1, 20, 15, 19, 4, 13, 11] + [-1]*100
last = 6
insert(23)
# print(TREE)
# insert(25)
# print(TREE)

print(dequeue())
print(TREE)
print(last) # 19는 쓰레기 값, last는 6번인 11까지
print(dequeue())
print(TREE)

# # 트리의 값이 정렬되어 출력되고 있음을 보여주는 코드
# arr = [3, 6, 1, 9, 10]
# last = 0
# TREE = [-1] * 100
# for d in arr:
#     insert(d)
#     print(TREE)
#
# for i in range(last):
#     print(dequeue())