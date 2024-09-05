def count_kkang(lst):
    c = 0
    for e in lst:
        if e[0] <= 0:
            c += 1
    return c

def kkang(idx, eggs):
    global result
    # 종료조건
    if idx == N:
        cnt = count_kkang(eggs)
        if cnt > result:
            result = cnt
        return

    if eggs[idx][0] <= 0:  # 내가 들고 있는 계란이 깨졌을 때
        return

    for i in range(N):
        if eggs[i][0] <= 0:
            continue

        if i != idx and eggs[i][0] > 0:
            eggs[idx][0] = EGGS[idx][0] - EGGS[i][1] # 내 내구도
            eggs[i][0] = EGGS[i][0] - EGGS[idx][1] # 남의 내구도
            if eggs[i][0] <= 0:
                cnt = count_kkang(eggs)
                if cnt > result:
                    result = cnt
                continue
            kkang(idx+1, eggs)

            eggs[idx][0] += EGGS[i][1]
            eggs[i][0] += EGGS[idx][1]

        # 내 계란 살아있는데 깰 게 깨져있을때
        # 내 계란 죽고 깰 것도 죽고

import copy
N = int(input())
EGGS = [list(map(int, input().split())) for _ in range(N)]
# 내구도 : EGGS[0], 무게 : EGGS[1]
eggs = copy.deepcopy(EGGS)
result = 0
kkang(0, eggs)

print(result)
