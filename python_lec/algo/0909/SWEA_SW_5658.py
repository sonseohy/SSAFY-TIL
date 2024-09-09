import sys
sys.stdin = open('input.txt', 'r')

def hextodec(hex_lst):
    global result
    for h in hex_lst:
        if int(h, 16) not in result:    # 16진수를 10진수로 바꿔 result에 없는 값만 append
            result.append(int(h, 16))


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    numbers = input()

    result = []  # 생성 가능한 수를 내림차순 나열해 10진수로 저장
    PW = [] # 한 변에 배치하는 16진수 저장

    for i in range(N//4):
        for j in range(4):
            PW.append(numbers[i+j * (N // 4):i+j * (N // 4) + N // 4])
        if len(PW[3]) < N//4:
            PW[3] += numbers[0:N//4-len(PW[3])]
        hextodec(PW)
        PW = []

    result.sort(reverse=True)   # 내림차순 정렬

    # 최종 출력 : K번째로 큰 수를 10진 수로 만든 수
    print(f'#{test_case} {result[K-1]}')