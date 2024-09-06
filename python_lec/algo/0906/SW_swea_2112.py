# 특성 A : 0, 특성 B : 1
import copy

def test(cell, lst):
    value = 0
    for j in range(W):
        for i in range(D):
            if lst[i][j] == cell:
                value += 1
            else:
                value = 0
        if value < K:
            if cell == 0:
                test(1, lst)
            return False
    return True

def change(cell, lst, idx):
    global result
    t = []

    if idx == D:
        return

    check = test(cell, lst)
    if check:
        if result > idx:
            result = idx

    else:
        t = lst[idx]
        for k in [0,1]:
            lst[idx] = [k]*W
            c = test(cell, lst)
            if c:
                break
        if check:
            if result > idx:
                result = idx
                return
        lst[idx] = t
        change(cell, lst, idx+1)

T = int(input())

for test_case in range(1, T+1):
    D, W, K = map(int, input().split())
    PROTECTOR = [list(map(int, input().split())) for _ in range(D)]
    protector = copy.deepcopy(PROTECTOR)
    result = 14
    change(0, protector, 0)

    print(f'#{test_case} {result}')