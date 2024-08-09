def group(n):




# 1 : 가위, 2 : 바위, 3 : 보
# 같으면 번호 작은 쪽 승자
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    group(N//2)