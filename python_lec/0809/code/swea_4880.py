# 가위바위보 카드의 승자를 찾는 함수
def card_comparison(i, j):
    # 비긴 경우
    if arr[i] == arr[j]:
            return i
    # i가 이긴 경우 : return i, j가 이긴 경우 : reutrn j
    elif (arr[i] == 1 and arr[j] == 3) or (arr[i] == 2 and arr[j] == 1) or (arr[i] == 3 and arr[j] == 2):
        return i
    else:
        return j
            
def group(i, j):
    # 카드가 한개일 때
    if i == j:
        return i
    # 카드가 두개 남을 때
    elif i + 1 == j:
        return card_comparison(i, j)
    else:
        mid_idx = (i + j) // 2
        g1 = group(i, mid_idx)
        g2 = group(mid_idx + 1, j)
        return card_comparison(g1, g2)

# 1 : 가위, 2 : 바위, 3 : 보
# 같으면 번호 작은 쪽 승자
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    winner = group(1, N)

    print(f'#{test_case} {winner}')

'''
# 시도2 제한시간 초과
# 가위바위보 카드의 승자를 찾는 함수
def card_comparison(i, j):
    # 비긴 경우
    if arr[i] % arr[j] == 0:
            return i
    # i가 이긴 경우 : return i, j가 이긴 경우 : reutrn j
    else:
        if arr[i] == 1:
            if arr[j] == 3:
                return i
            elif arr[j] == 2:
                return j
        if arr[i] == 2:
            if arr[j] == 1:
                return i
            elif arr[j] == 3:
                return j
        if arr[i] == 3:
            if arr[j] == 2:
                return i
            elif arr[j] == 1:
                return j
            
def group(i, j):
    # 카드가 한개일 때
    if i == j:
        return i
    # 카드가 두개 남을 때
    elif i + 1 == j:
        return card_comparison(i, j)
    else:
        mid_idx = (i + j) // 2
        g1 = group(1, mid_idx)
        g2 = group(mid_idx + 1, j)
        return card_comparison(g1, g2)

# 1 : 가위, 2 : 바위, 3 : 보
# 같으면 번호 작은 쪽 승자
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    idx = (1 + N) // 2
    g1_winner = group(1,idx)
    g2_winner = group(idx + 1, N)

    if g1_winner > g2_winner:
        print(f'#{test_case} {g1_winner}')
    else:
        print(f'#{test_case} {g2_winner}')
'''

'''
# 시도 1
# 가위바위보 카드의 승자를 찾는 함수
def card_comparison(i, j):
    # 비긴 경우
    if arr[i] % arr[j] == 0:
            return i
    # i가 이긴 경우 : return i, j가 이긴 경우 : reutrn j
    else:
        if arr[i] == 1:
            if arr[j] == 3:
                return i
            elif arr[j] == 2:
                return j
        if arr[i] == 2:
            if arr[j] == 1:
                return i
            elif arr[j] == 3:
                return j
        if arr[i] == 3:
            if arr[j] == 2:
                return i
            elif arr[j] == 1:
                return j
            
def group(i, j):
    if j <= 2:
        win = card_comparison(i, j)
        if win =='i':
            return i
        elif win == 'j':
            return j

    return (i+j) // 2

# 1 : 가위, 2 : 바위, 3 : 보
# 같으면 번호 작은 쪽 승자
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    idx = (1 + N) // 2
    g1_winner = group(1,idx)
    g2_winner = group(idx + 1, N)

    if g1_winner > g2_winner:
        print(f'#{test_case} {g1_winner}')
    else:
        print(f'#{test_case} {g2_winner}')

'''