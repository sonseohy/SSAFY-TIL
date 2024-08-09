T = int(input())

for tc in range(1, T + 1):
    input_s = input().split()

    pos_b = pos_o = 1   # 로봇 B, O의 현재 위치
    total = 0           # 걸리는 최소 시간
    oposite_time = 0    # 이전에 걸린 시간
    pre_robot = input_s[1]  # 이전의 로봇 정보

    for i in range(1, len(input_s), 2):
        robot = input_s[i]
        pos = int(input_s[i+1])     # 가야할 위치

        if robot == 'B':
            time = abs(pos-pos_b)
            pos_b = pos
        else:   # robot == 'O'
            time = abs(pos - pos_o)
            pos_o = pos

        if pre_robot == robot:
            total += time + 1
            oposite_time += time + 1
        else:
            if oposite_time - time > 0:
                time = 1
            else:
                time = time - oposite_time + 1
            total += time
            oposite_time = time
            pre_robot = robot
    print(f'#{tc} {total}')