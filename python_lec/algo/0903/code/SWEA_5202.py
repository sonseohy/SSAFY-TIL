T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    timetable = [list(map(int, input().split())) for _ in range(N)]
    timetable.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    end = -1
    for time in timetable:
        if time[0] >= end:
            cnt += 1
            end = time[1]
    # 바보
    print(f'#{test_case} {cnt}')