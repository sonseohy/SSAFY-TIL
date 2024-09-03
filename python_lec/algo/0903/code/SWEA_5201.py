# N개의 컨테이너, M대의 트럭
# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다.
# 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    W = [0] + list(map(int, input().split()))
    T = list(map(int, input().split()))

    sum_v = 0
    check = [0] * (N+1) # 사용한 화물 컨테이너 체크
    for i in range(M):
        max_idx = 0
        for j in range(1, N+1):
            if W[j] <= T[i] and check[j] == 0 and W[max_idx] <= W[j]:   # 트럭의 적재 용량을 넘지않는 값 중 최대값 컨테이너 찾아 배정
                max_idx = j
        if max_idx == 0:
            continue
        check[max_idx] = 1
        sum_v += W[max_idx]

    print(f'#{test_case} {sum_v}')