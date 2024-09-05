def recur(level, lst1, lst2):
    global result
    if level == n:
        sumV = 0
        for i in lst2:
            sumV += s[i]
        if sumV >= b and sumV < result:
            result = sumV
        return
    recur(level + 1, lst1 + [level], lst2)
    recur(level + 1, lst1, lst2 + [level])

# bit 이용
def solve():
    global result
    # 모든 부분집합 구하기
    for i in range(2**n): # for i in range(1<<n):
        value = i
        sumV = 0
        for j in range(n):
            # value의 j번째 bit를 구해서 1이면
            if value&0x1:   # i의 0번째 비트를 구해서 1이면
                sumV += s[j]
            value = value >> 1
        if sumV >= b and sumV < result:
            result = sumV

t = int(input())
for tc in range(1, t + 1):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    result = sum(s)
    # recur(0, [], [])
    solve()
    print(f'#{tc} {result - b}')