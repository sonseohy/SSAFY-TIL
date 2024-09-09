import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split())

    if A < 1 or B < 2 or C < 3:     # A < B < C 구조를 만들 수 없는 케이스를 처리
        print(f'#{test_case} -1')
        continue

    eat = 0     # 먹은 사탕 개수
    # 설계 : B가 C 이상일 때, B = C - 1 이라면 최소 개수
    if B >= C:
        eat += B - (C - 1)  # 차이만큼 먹음
        B = C - 1   # 먹고 B값 초기화
    #       A가 B 이상일 때, A = B - 1 이라면 최소 개수
    if A >= B:
        eat += A - (B - 1)  # 차이만큼 먹음
        A = B - 1

    print(f'#{test_case} {eat}')