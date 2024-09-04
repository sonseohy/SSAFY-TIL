def binary_search(low, high, target):
    global check
    # 값을 찾지 못했을 때
    if low > high:
        return 0

    mid = (low+high) // 2

    if A[mid] == target:
        return 1

    elif A[mid] > target:
        if check == 1:
            return 0
        check = 1
        return binary_search(low, mid-1, target)

    else:
        if check == 2:
            return 0
        check = 2
        return binary_search(mid+1, high, target)


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    result = 0
    for i in range(M):
        check = 0  # 양쪽구간이 번갈아 선택되고 있는지 확인
        cnt = binary_search(0, N-1, B[i])   # 오답 : 인덱스 끝 값을 보내야 하니까 N-1
        result += cnt

    print(f'#{test_case} {result}')