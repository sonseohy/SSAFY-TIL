def kkang(idx, eggs):
    global result

    # 종료조건
    if idx == N:
        cnt = 0
        for e in eggs:
            if e[0] <= 0:
                cnt += 1
        if cnt > result:
            result = cnt
        return

    if eggs[idx][0] <= 0:  # 내가 들고 있는 계란이 깨진 상태일 때 다음 계란 선택
        kkang(idx + 1, eggs)
        return

    check = True
    for i in range(N):
        if eggs[i][0] <= 0: # 다음 깰 계란이 깨져있을 때 다음 계란으로 넘어감
            continue
        if i != idx and eggs[i][0] > 0:
            check = False
            # 계란 깨기
            eggs[idx][0] -= eggs[i][1]  # 들고있는 계란 내구도 감소
            eggs[i][0] -= eggs[idx][1]  # 상대 내구도 감소

            # 다음 계란 선택
            kkang(idx + 1, eggs)

            # 계란 상태 복구
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

    if check == True:  # 더 이상 깰 계란이 없을때
        kkang(idx + 1, eggs)


N = int(input())
EGGS = [list(map(int, input().split())) for _ in range(N)]
# 내구도 : EGGS[0], 무게 : EGGS[1]
result = 0
kkang(0, EGGS)
print(result)