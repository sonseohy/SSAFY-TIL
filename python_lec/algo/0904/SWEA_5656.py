# 중복순열
T = int(input())

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    BREAKOUT = [list(map(int, input().split())) for _ in range(H)]

