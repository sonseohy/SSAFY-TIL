K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

cnt = 0
cut = max(LAN)
while cnt >= N:
    cut //= 2
    for i in range(K):
        cnt += LAN[i] // cut

print(cnt)