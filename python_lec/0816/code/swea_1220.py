# Blue = N = 위, Red = S = 밑
# 1 = N극 성질, 2 = S극 성질

T = 1

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_arr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i].append(arr[j][i])


    for a in new_arr:
        cnt_1 = 0
        cnt_2 = 0
        for k in range(N):
            print(k)
            if a[k] == 1:
                cnt_1 += 1
            if cnt_1 > 1 and a[k] == 2:
                cnt_2 += 1
    print(f'{cnt_1} {cnt_2}')

    # for j in range(N):
    #     counts = [0, 0]
    #     for i in range(N):
    #         if arr[i][j] == 1:
    #             counts[0] += 1
    #             print('1 : ', i, j, arr[i][j])
    #         if counts[0] > 1 and arr[i][j] == 2:
    #             counts[1] += 1
    #             print('2 : ', i, j, arr[i][j])


    # print(f'#{test_case} {cnt}')