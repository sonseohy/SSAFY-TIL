def same_cnt(a, idx, pre):
    global min_cnt
    cnt = 0
    if pre == 'W': # W or B

        cnt += a[idx].count('W')
    
        for k in range(idx + 1, N - 1):
            for j in range(M):
                if k == N - 1:
                    if arr[idx][j] != 'B':
                        cnt += 1
                    
                if a[k].count('W') == a[k].count('B'):
                    continue
                if a[k].count('W') > a[k].count('B'):
                    if arr[k][j] != 'W':
                        cnt += 1
                    pre = 'W'
                    return cnt
                elif a[k].count('W') < a[k].count('B'):
                    if arr[k][j] != 'B':
                        cnt += 1
                    pre = 'B'
                    return cnt
                else:
                    cnt += same_cnt(a, k, pre)
                    pre = 'B'
                    break
    elif pre == 'B': # B or R
        cnt += a[idx].count('B')
        for k in range(idx + 1, N - 1):
            for j in range(M):
                if a[k].count('B') > a[k].count('R'):
                    if arr[k][j] != 'B':
                        cnt += 1
                    pre = 'B'
                    return cnt
                elif a[k].count('B') < a[k].count('R'):
                    if arr[k][j] != 'R':
                        cnt += 1
                    pre = 'R'
                    return cnt
                else:
                    min_cnt += same_cnt(a, k, pre)
                    break
    return cnt

def paint(a):
    global min_cnt
    for i in range(1, N-1):
        for j in range(M):
            if i == 1:
                pre_color = 'W'

            if pre_color == 'W':
                if a[i].count('W') > a[i].count('B'):
                    if arr[i][j] != 'W':
                        min_cnt += 1
                    pre_color = 'W'
                elif a[i].count('W') < a[i].count('B'):
                    if arr[i][j] != 'B':
                        min_cnt += 1
                    pre_color = 'B'
                else:
                    min_cnt += same_cnt(a, i, pre_color)
                
            elif pre_color == 'B':
                if a[i].count('B') > a[i].count('R'):
                    if arr[i][j] != 'B':
                        min_cnt += 1
                    pre_color = 'B'
                elif a[i].count('B') < a[i].count('R'):
                    if arr[i][j] != 'R':
                        min_cnt += 1
                    pre_color = 'R'
                else:
                    min_cnt += same_cnt(a, i, pre_color)

            elif pre_color == 'R':
                if arr[i][j] != 'R':
                    min_cnt += 1

    return min_cnt
                    
    
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    cnt = 0
    min_cnt = 0
    for i in range(N):
        for j in range(M):
            if i == 0:
                if arr[i][j] != 'W':
                    cnt += 1
            elif i == N-1:
                if arr[i][j] != 'R':
                    cnt += 1
            else:
                cnt += paint(arr)

    print(f'#{test_case} {cnt}')


# 코드가 이상해졌어.. 너무 복잡해
# 밀고 다시 시작
'''
import copy

def count_color(lst):
    cnt_w = 0
    cnt_b = 0
    cnt_r = 0
                
    for j in range(M):
        if lst[j] == 'W':
            cnt_w += 1
        if lst[j] == 'B':
            cnt_b += 1
        if lst[j] == 'R':
            cnt_r += 1
    return cnt_w, cnt_b, cnt_r

def same_cnt(wbr):
    global pre_color
    min_c = 0
    tmp = copy.deepcopy(arr)
    if wbr[0] == wbr[1] or wbr[1] == wbr[2]:
        min_c += wbr[1]
        next_row = count_color(arr[i+1])
        for j in range(M):
            if next_row[0] < next_row[1] or next_row[2] < next_row[1]:
                if tmp[i+1][j] != 'B':
                    tmp[i+1][j] = 'B'
                    min_c += 1
                pre_color = 'B'
            elif next_row[0] > next_row[1]:
                if tmp[i+1][j] != 'W':
                    tmp[i+1][j] = 'W'
                    min_c += 1
                pre_color = 'W'
            elif next_row[2] > next_row[1]:
                if tmp[i+1][j] != 'R':
                    tmp[i+1][j] = 'R'
                    min_c += 1
                pre_color = 'R'           
        return min_c


def paint(i, cnt_wbr, pre):
    min_cnt = 0
    tmp = copy.deepcopy(arr)
 
    for j in range(M):
        if pre == 'W' and i == N - 2:               
            if tmp[i][j] != 'B':
                tmp[i][j] = 'B'
                min_cnt += 1
        elif pre == 'W' and i != N - 2:
            if cnt_wbr[0] > cnt_wbr[1]:
                if tmp[i][j] != 'W':
                    tmp[i][j] = 'W'
                    min_cnt += 1
            elif cnt_wbr[0] < cnt_wbr[1]:
                if tmp[i][j] != 'B':
                    tmp[i][j] = 'B'
                    min_cnt += 1
                    pre = 'B'
        elif pre == 'B':
            if cnt_wbr[1] > cnt_wbr[2]:
                if tmp[i][j] != 'B':
                    tmp[i][j] = 'B'
                    min_cnt += 1
                    pre = 'B'
            elif cnt_wbr[1] < cnt_wbr[2]:
                if tmp[i][j] != 'R':
                    tmp[i][j] = 'R'
                    min_cnt += 1
        elif pre == 'R':
            if tmp[i][j] != 'R':
                tmp[i][j] = 'R'
                min_cnt += 1

    return min_cnt


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    result = 0
    for i in range(N):
        for j in range(M):
            if i == 0:
                pre_color = 'W'
                if arr[i][j] != 'W':
                    arr[i][j] = 'W'
                    cnt += 1
            elif i == N-1:
                if arr[i][j] != 'R':
                    arr[i][j] = 'R'
                    cnt += 1
            else:
                cnt_wbr = count_color(arr[i])
                if same_cnt(cnt_wbr):
                    i += 1
                    cnt += same_cnt(cnt_wbr)
                    break
                cnt += paint(i, cnt_wbr, pre_color)
                break

    print(f'#{test_case} {cnt}')
'''

# 문제 4
# 테스트 케이스는 잘 작동하나 제출시 한 개의 테스트 케이스만 맞다고 하는 이유?
# 파란색을 한줄만 칠하는 것을 기준으로 짜진 코드
# WWWWW BBBBB BBBBB BBBBB RRRRR인 경우 바꾸지 않아도 되지만 최소 횟수가 10으로 나와버림
'''
import copy
def paint(blue):
    tmp = copy.deepcopy(arr)
    min_cnt = 0
    for i in range(1, N-1):
        for j in range(M):
            if i == blue:
                if tmp[i][j] != 'B':
                    tmp[i][j] = 'B'
                    min_cnt += 1
            elif i < blue:
                if tmp[i][j] != 'W':
                    tmp[i][j] = 'W'
                    min_cnt += 1
            elif i > blue:
                if tmp[i][j] != 'R':
                    tmp[i][j] = 'R'
                    min_cnt += 1
    return min_cnt


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    result = 2501
    for i in range(N):
        for j in range(M):
            if i == 0:
                if arr[i][j] != 'W':
                    arr[i][j] = 'W'
                    cnt += 1
            elif i == N-1:
                if arr[i][j] != 'R':
                    arr[i][j] = 'R'
                    cnt += 1
            else:
                blue = i
                min_paint = paint(blue)
                if min_paint < result:
                    result = min_paint
                break
    cnt += result
    print(f'#{test_case} {cnt}')
'''

# 문제 3
# 함수로 precolor가 w, b일때 합치고 싶었는데 실패
# 해결책? 갈아엎고 파랑`이 들어갈 자리를 먼저 찾는 코드로 전환
'''
def paint(lst, pre_color):
    global cnt
    
    color_dict = {'w': 0, 'B':0, 'R':0}

    for k in range(M):
        color_dict[lst[k]] += 1

    
    if pre_color == 'W':   # 'W' or 'B'
        if cnt_w > cnt_b:
            for k in range(M):
                if lst[k] != 'W':
                    lst[k] = 'W'
                    cnt += 1
        elif cnt_w == cnt_b:
            pass
        else:
            for k in range(M):
                if lst[k] != 'B':
                    lst[k] = 'B'
                    cnt += 1
    elif pre_color == 'B':  # 'B' or 'R'
        if cnt_b > cnt_r:
            for k in range(M):
                if lst[k] != 'B':
                    lst[k] = 'B'
                    cnt += 1
        elif cnt_b == cnt_r:
            pass
        else:
            for k in range(M):
                if lst[k] != 'R':
                    lst[k] = 'R'
                    cnt += 1


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if i == 0 and arr[i][j] != 'W':
                arr[i][j] = 'W'
                cnt += 1
            elif i == N-1 and arr[i][j] != 'R':
                arr[i][j] = 'R'
                cnt += 1
            else:
                paint(arr[i], arr[i-1][j])

    print(f'#{test_case} {cnt}')

'''
# 2
# 문제점 : 함수 안에서도 반복되는 코드가 많음
# 이전 색이 w인 경우, b인 경우 색 카운트를 어느 변수에 하느냐를 제외하고는 작동 방식이 같음
# 해결법? count 리스트를 만들어서 인덱스 0에는 w, 1에는 b, 2에는 r을 카운트 하는 방식으로 함수 수정
'''
def paint(lst, pre_color):
    global cnt

    cnt_w = 0
    cnt_b = 0
    cnt_r = 0

    for k in range(M):
        if lst[k] == 'W':
            cnt_w += 1
        if lst[k] == 'B':
            cnt_b += 1
        if lst[k] == 'R':
            cnt_r += 1

    if pre_color == 'W':   # 'W' or 'B'
        if cnt_w > cnt_b:
            for k in range(M):
                if lst[k] != 'W':
                    lst[k] = 'W'
                    cnt += 1
        elif cnt_w == cnt_b:
            pass
        else:
            for k in range(M):
                if lst[k] != 'B':
                    lst[k] = 'B'
                    cnt += 1
    elif pre_color == 'B':  # 'B' or 'R'
        if cnt_b > cnt_r:
            for k in range(M):
                if lst[k] != 'B':
                    lst[k] = 'B'
                    cnt += 1
        elif cnt_b == cnt_r:
            pass
        else:
            for k in range(M):
                if lst[k] != 'R':
                    lst[k] = 'R'
                    cnt += 1


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if i == 0 and arr[i][j] != 'W':
                arr[i][j] = 'W'
                cnt += 1
            elif i == N-1 and arr[i][j] != 'R':
                arr[i][j] = 'R'
                cnt += 1
            else:
                paint(arr[i], arr[i-1][j])
                break

    print(f'#{test_case} {cnt}')
'''

# 1
# 문제점 : w와 b 갯수가 같거나, b와 r 개수가 같은 경우 처리가 없음
# 굳이 배열의 색을 바꾸지 않아도 됨, 카운트만 제대로 해서 출력해도 상관 X
# 해결법? 최소 색칠 경우를 구하는 경우를 함수로 따로 구현해보자
'''
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    cnt = 0
    for i in range(N):
        w_cnt = 0
        b_cnt = 0
        r_cnt = 0
        for j in range(M):
            if i == 0 and arr[i][j] != 'W':
                arr[i][j] = 'W'
                cnt += 1
            elif i == N-1 and arr[i][j] != 'R':
                arr[i][j] = 'R'
                cnt += 1
            else:
                if arr[i][j] == 'W':
                    w_cnt += 1
                if arr[i][j] == 'B':
                    b_cnt += 1
                if arr[i][j] == 'R':
                    r_cnt
        if w_cnt == b_cnt or b_cnt == r_cnt:

        if 0 < i < N-1 and arr[i-1][0] == 'W':   # 'W' or 'B'
            if w_cnt > b_cnt:
                for k in range(M):
                    if arr[i][k] != 'W':
                        arr[i][k] = 'W'
                        cnt += 1
            else:
                for k in range(M):
                    if arr[i][k] != 'B':
                        arr[i][k] = 'B'
                        cnt += 1
        elif 0 < i < N-1 and arr[i-1][0] == 'B':  # 'B' or 'R'
            if b_cnt > r_cnt:
                for k in range(M):
                    if arr[i][k] != 'B':
                        arr[i][k] = 'B'
                        cnt += 1
            else:
                for k in range(M):
                    if arr[i][k] != 'R':
                        arr[i][k] = 'R'
                        cnt += 1
        print(cnt)
    print(f'#{test_case} {cnt}')
'''