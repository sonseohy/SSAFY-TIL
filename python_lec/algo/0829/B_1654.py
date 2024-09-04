K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

start = 1
end = max(LAN)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(K):
        cnt += LAN[j] // mid
    if cnt > N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
