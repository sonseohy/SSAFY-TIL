# 무승부인 경우 0을 출력
def babygin(lst):
    for k in range(10):
        if lst[k] == 3:
            return True

    for r in range(8):
        if lst[r] > 0 and lst[r+1] > 0 and lst[r+2] > 0:
            return True

    return False

T = int(input())

for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10

    # p1_lst = []
    # p2_lst = []
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            p1[cards[i]] += 1
            # p1_lst.append(cards[i])
            if babygin(p1):
                winner = 1
                break
        else:
            p2[cards[i]] += 1
            # p2_lst.append(cards[i])
            if babygin(p2):
                winner = 2
                break

    print(f'#{test_case} {winner}')
    # print(p1_lst)
    # print(p2_lst)