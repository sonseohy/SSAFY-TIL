# L, M, S의 차이를 return
# 단 구간을 만들 수 없으면 -1을 return
def cal(m_s, m_e):
    small = sum(counts[minCarrot:m_s])
    medium = sum(counts[m_s:m_e+1])
    large = sum(counts[m_e+1:maxCarrot+1])

    if small == 0 or medium == 0 or large == 0:
        return -1
    if small > N//2 or medium > N//2 or large > N//2:
        return -1

    return max(small, medium, large) - min(small, medium, large)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    counts = [0] * 31
    for c in arr:
        counts[c] += 1

    minCarrot = min(arr)
    maxCarrot = max(arr)
    min_v = 1001
    for m_start in range(minCarrot+1, maxCarrot):
        for m_end in range(m_start, maxCarrot):
            t = cal(m_start, m_end)
            if t == -1:
                continue
            if min_v > t:
                min_v = t
    if min_v == 1001:
        min_v = -1
    print(f'#{test_case} {min_v}')