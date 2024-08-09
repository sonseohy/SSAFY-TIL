T = int(input())

for test_case in range(1, T + 1):
    arr = input().split()

    pos_o = 1   # 현재 오렌지 위치
    pos_b = 1   # 현재 블루 위치

    pre_robot = arr[1]  # 이전 로봇이 무엇인지
    oposite_time = 0    # 이전 로봇에 얼만큼 갔는지 시간
    total = 0   # 전체 소요시간

    for i in range(1, len(arr), 2): # 1, 3, 5, 7 (홀수 인덱스, 로봇)
        robot = arr[i]  # B
        num = int(arr[i+1]) # 2

        if robot == 'B':
            # 버튼 위치까지 이동 후 시간 계산
            pos_b = num
            total += num
        else: # robot == 'O'
            # 버튼 위치까지 이동 후 시간 계산
            pos_o = num
            total += num

        if pre_robot == robot:
            # 바로 앞의 로봇이 나랑 같은지 다른지
            total += num - oposite_time + 1
        else:
            if num  < oposite_time:
                pass

            else:
                pass


        pre_robot = robot # 이전 로봇을 현재 로봇으로 초기화
        oposite_time = num