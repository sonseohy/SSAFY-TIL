import copy

def test(lst):
    pre_n = lst[0][0]
    for j in range(W):
        a = 0
        b = 0
        for i in range(D):
            if lst[i][j] == 0:
                if a != 0 and pre_n == 1:
                    a = 0
                a += 1
                pre_n = 0
            else:
                if b != 0 and pre_n == 0:
                    b = 0
                b += 1
                pre_n = 1
            if a >= K or b >= K:
                break
        if a < K and b < K:
            return False 
    return True

def change(cell, lst, idx):
    global result, cnt
    if idx == D:
        if test(lst):
            result = min(result, cnt)
        return
    
    if cnt >= result:
        return
    
    if idx == 0:
        if test(lst):
            result = min(result, cnt)
            return

    # 원본 리스트 저장
    tmp = lst[idx]
    
    for k in [0, 1]:     # 약품 처리
        lst[idx] = [k] * W
        cnt += 1
        change(k, lst, idx + 1)
        cnt -= 1
    
    # 원본 리스트로 복구
    lst[idx] = tmp
    change(cell, lst, idx + 1)

# # 특성 A : 0, 특성 B : 1
# import copy

# def test(cell, lst):
#     for j in range(W):
#         value = 0
#         for i in range(D):
#             if lst[i][j] == cell:
#                 value += 1
#             else:
#                 value = 0
#         if value < K:
#             if cell == 0:
#                 test(1, lst)
#             return False 
#     if result > cnt:
#         result = cnt
#     return True

# def change(cell, lst, idx):
#     global result, cnt
#     t = []

#     if idx == D:
#         return
    
#     for d in range(D):
#         check = test(cell, lst)
#         if check:
#             break
#         else:
#             t = lst[idx]        # 원복을 위해 원본 리스트 저장
#             cnt += 1
#             for k in [0,1]:     # 약품 처리
#                 lst[idx] = [k]*W
#                 c = test(cell, lst)
#                 if c:
#                     break
#                 change(cell, lst, d+1)
#         change(cell, lst, idx+1)
#         lst[idx] = t
#         cnt -= 1

T = int(input())

for test_case in range(1, T+1):
    D, W, K = map(int, input().split())
    PROTECTOR = [list(map(int, input().split())) for _ in range(D)]
    protector = copy.deepcopy(PROTECTOR)
    result = 14
    cnt = 0
    change(0, protector, 0)

    print(f'#{test_case} {result}')
