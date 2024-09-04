# 자성이 다를 경우 반대 방향으로 1칸 회전, 같으면 회전 X
# N극 : 0, S극 : 1

def turn_mag(d, cur_m, next_m):
    if d == 1:  # 시계 방향
        end = cur_m.pop()
        cur_m.insert(0, end)

        start = next_m.pop(0)
        next_m.append(start)

    elif d == -1:  # 반시계 방향
        start = cur_m.pop(0)
        cur_m.append(start)

        end = next_m.pop()
        next_m.insert(0, end)

T = int(input())

for test_case in range(1, T+1):
    K = int(input())    # 자석 회전 횟수
    magnetics = [list(map(int, input().split())) for _ in range(4)]
    turn = [list(map(int, input().split())) for _ in range(K)]

    able = [False] * 4

    for i in range(K):
        m = turn[i][0] - 1  # 회전할 자석
        d = turn[i][1]  # 회전 방향

        able = [False] * 4
        for j in range(3):
            if magnetics[j][2] != magnetics[j + 1][6]:
                able[j] = True

        #회전할 자석을 먼저 돌림

        for n in range(4):
            if able[n] == True:
                turn_mag(d, magnetics[n], magnetics[n + 1])

        for x in range(4):
            print(*magnetics[x])


        # if 0 <= m + 1 < 4 and magnetics[m][2] != magnetics[m + 1][6]:  # 오른쪽 비교
        #     turn_mag(d, magnetics[m], magnetics[m+1])
        #     m = (m + 1) % 4
        #
        # elif 0 <= m - 1 < 4 and magnetics[m][6] != magnetics[m - 1][2]:  # 왼쪽 비교
        #     turn_mag(d, magnetics[m], magnetics[m+1])
        #     m = (m + 1) % 4



# # 시도 1 : index로.. 실패
# # 자성이 다를 경우 반대 방향으로 1칸 회전, 같으면 회전 X
# # 시계방향 : 1, 반시계 방향 : -1
# # N극 : 0, S극 : 1
# # 자석 리스트 0번 : 화살표 위치, 2번 : 오른쪽 90도, 6번 : 왼쪽 90도
#
# def turn_mag(d, m):
#     if d == 1:  # 시계 방향
#         # idx : mag는 +1씩, mag+1은 -1씩
#         point[m] += 1
#         point[m + 1] -= 1
#         l_idx[m] += 1
#         l_idx[m + 1] -= 1
#         r_idx[m] += 1
#         r_idx[m + 1] -= 1
#     elif d == -1:  # 반시계 방향
#         # idx : mag는 -1씩, mag+1은 +1씩
#         point[m] -= 1
#         point[m + 1] += 1
#         l_idx[m] -= 1
#         l_idx[m + 1] += 1
#         r_idx[m] -= 1
#         r_idx[m + 1] += 1
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     K = int(input())    # 자석 회전 횟수
#     magnetics = [list(map(int, input().split())) for _ in range(4)]
#     turn = [list(map(int, input().split())) for _ in range(K)]
#
#     point = [0] * 4 # 현재 자석 상단의 index
#     l_idx = [2] * 4 # 자석 오른쪽 index
#     r_idx = [6] * 4 # 자석 왼쪽 index
#
#     for i in range(K):
#         m = turn[i][0] - 1  # 회전할 자석
#         d = turn[i][1]      # 회전 방향
#         check = [0]*4
#         while 0 not in check:
#             if 0 <= m+1 < 4 and magnetics[m][l_idx[m]] != magnetics[m + 1][r_idx[m+1]]:  # 오른쪽 비교
#                 turn_mag(d, m)
#                 m = (m+1) % 4
#             elif 0 <= m-1 < 4 and magnetics[m][r_idx[m]] != magnetics[m - 1][l_idx[m+1]]:  # 왼쪽 비교
#                 turn_mag(d, m)
#                 m = (m+1) % 4
#             check[m] = 1
#
#     print(point)
