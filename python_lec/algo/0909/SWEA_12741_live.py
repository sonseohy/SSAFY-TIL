import sys
sys.stdin = open('input.txt', 'r')

# 시간 초과 발생
T = int(input())

for test_case in range(1, T+1):
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구 시간이 시작점
    start = max(A, C)
    # 먼저 꺼진 전구 시간이 끝점
    end = min(B, D)


    result = end - start
    if result <= 0: # 안 겹치는 경우
        result = 0

    print(f'#{test_case} {result}')

# 출력이 많으면 몰아서 하자 - input/output 변환 시간, Buffer
# for문에서 50000번 출력하는 것보다 50000개의 결과를 리스트에 저장해서 한번에 출력하는 것이 시간이 훨씬 적게 걸림


# 결과를 모아서 출력
T = int(input())
result_lst = []     # 결과들을 저장

for test_case in range(1, T+1):
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구 시간이 시작점
    start = max(A, C)
    # 먼저 꺼진 전구 시간이 끝점
    end = min(B, D)

    result = end - start
    if result <= 0: # 안 겹치는 경우
        result = 0

    result_lst.append(result)

for index, result in enumerate(result_lst):
    print(f'#{index+1} {result}')