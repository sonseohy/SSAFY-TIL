T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    ROUTES = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    counts = [0] * 5001

    for a, b in ROUTES:
        for i in range(a, b+1):
            counts[i] += 1
    
    result = []
    for c in C:
        result.append(counts[c])

    print(f'#{test_case}', *result)


"""
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    ROUTES = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    counts = [0] * (P+1)

    for a, b in ROUTES:
        for i in range(a, b+1):
            counts[i] += 1
    
    print(f'#{test_case}', *counts[1:])

# 런타임 에러
# b가 p보다 클 때 문제가 발생, counts[b]에서 인덱스가 리스트의 범위를 넘어감
"""