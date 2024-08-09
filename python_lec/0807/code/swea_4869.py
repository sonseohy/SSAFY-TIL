def paper(n):
    for i in range(n // 10):
        if n == 1:
            return 1
        elif n == 2:
            return 3
        else:
            result = paper(n-1) + paper(n-2) * 2
    return result


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    print(f'#{test_case} {paper(N)}')