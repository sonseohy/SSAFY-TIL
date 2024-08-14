T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 1
    max_v = 0
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            cnt += 1
        else:
            cnt = 1
        if max_v < cnt:
            max_v = cnt
    if cnt > 1 and max_v < cnt:
        max_v = cnt
    print(f'#{test_case} {max_v}')