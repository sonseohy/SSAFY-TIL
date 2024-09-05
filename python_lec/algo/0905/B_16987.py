# GPT code
# def count_kkang(lst):
#     c = 0
#     for e in lst:
#         if e[0] <= 0:  # 계란이 깨졌다면
#             c += 1
#     return c

# def kkang(idx, eggs):
#     global result
    
#     # 종료 조건: 모든 계란을 시도했을 때
#     if idx == N:
#         cnt = count_kkang(eggs)
#         if cnt > result:
#             result = cnt
#         return

#     # 현재 계란이 이미 깨졌다면 다음 계란으로 이동
#     if eggs[idx][0] <= 0:
#         kkang(idx + 1, eggs)
#         return

#     # 다른 계란과 충돌 시뮬레이션
#     has_egg = False
#     for i in range(N):
#         if i != idx and eggs[i][0] > 0:
#             has_egg = True
#             # 충돌 시계란 상태 업데이트
#             eggs[idx][0] -= eggs[i][1]
#             eggs[i][0] -= eggs[idx][1]
            
#             # 충돌 후 상태로 재귀 호출
#             kkang(idx + 1, eggs)
            
#             # 원상복구
#             eggs[idx][0] += eggs[i][1]
#             eggs[i][0] += eggs[idx][1]
    
#     # 충돌을 시도하지 않은 경우에도 다음 계란으로 이동
#     if not has_egg:
#         kkang(idx + 1, eggs)

# import copy

# N = int(input())
# EGGS = [list(map(int, input().split())) for _ in range(N)]
# eggs = copy.deepcopy(EGGS)
# result = 0

# kkang(0, eggs)

# print(result)


# def count_kkang(lst):
#     c = 0
#     for e in lst:
#         if e[0] <= 0:
#             c += 1
#     return c

# def kkang(idx, eggs):
#     global result
#     # 종료조건
#     if idx == N:
#         cnt = count_kkang(eggs)
#         if cnt > result:
#             result = cnt
#         return

#     if eggs[idx][0] <= 0:  # 내가 들고 있는 계란이 깨졌을 때
#         kkang(idx + 1, eggs)
#         return

#     for i in range(N):
#         if eggs[i][0] <= 0:
#             continue

#         if i != idx and eggs[i][0] > 0:
#             eggs[idx][0] = EGGS[idx][0] - EGGS[i][1] # 내 내구도
#             eggs[i][0] = EGGS[i][0] - EGGS[idx][1] # 남의 내구도
#             if eggs[i][0] <= 0:
#                 cnt = count_kkang(eggs)
#                 if cnt > result:
#                     result = cnt
#                 eggs[idx][0] += EGGS[i][1]
#                 eggs[i][0] += EGGS[idx][1]

#                 continue

#             kkang(idx+1, eggs)

#             eggs[idx][0] += EGGS[i][1]
#             eggs[i][0] += EGGS[idx][1]

#         # 내 계란 살아있는데 깰 게 깨져있을때
#         # 내 계란 죽고 깰 것도 죽고

# import copy
# N = int(input())
# EGGS = [list(map(int, input().split())) for _ in range(N)]
# # 내구도 : EGGS[0], 무게 : EGGS[1]
# eggs = copy.deepcopy(EGGS)
# result = 0

# kkang(0, eggs)

# print(result)

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
        kkang(idx + 1, eggs)
        return

    for i in range(N):
        if eggs[i][0] <= 0:
            continue

        if i != idx and eggs[i][0] > 0:

            # 계란을 깨기
            eggs[idx][0] -= EGGS[i][1]  # 내구도 감소
            eggs[i][0] -= EGGS[idx][1]  # 상대 내구도 감소

            # 재귀 호출
            kkang(idx + 1, eggs)

            # 계란 상태 복구
            eggs[idx][0] += EGGS[i][1]
            eggs[i][0] += EGGS[idx][1]

        # 내 계란 살아있는데 깰 게 깨져있을때
        # 내 계란 죽고 깰 것도 죽고
    kkang(idx + 1, eggs)

import copy
N = int(input())
EGGS = [list(map(int, input().split())) for _ in range(N)]
# 내구도 : EGGS[0], 무게 : EGGS[1]
eggs = copy.deepcopy(EGGS)
result = 0

kkang(0, eggs)

print(result)