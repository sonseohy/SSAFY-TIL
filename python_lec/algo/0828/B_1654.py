def find(v):
    start = 0
    end = N - 1
    while m <= N:
        m = (start + end) // 2
        if key == arr[m]:
            return m
        if key > arr[m]:
            start = m + 1
        else:  # if key < arr[m]:
            end = m - 1
    return -1

K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

cnt = 0
cut = max(LAN)
while cnt >= N:
    cut //= 2
    for i in range(K):
        cnt += LAN[i] // cut

print(cnt)