T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    result = []

    for i in range(1, N+1):
        lst = []
        for j in range(i):
            if j == 0 or j == i - 1:
                lst.append(1)
            else:
                lst.append(result[i-2][j-1] + result[i-2][j])
        result.append(lst)

    print(f'#{test_case}')
    for r in result:
        print(*r)

# 재귀 (참고)
'''
def pascal(i):
    if i == 1:
        return [1]
    elif i == 2:
        return [1, 1]
    else:
        lst = []
        for j in range(i-2):
            lst.append((pascal(i-1)[j] + pascal(i-1)[j+1]))

        return [1] + lst + [1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}')
    for i in range(1, N+1):
        print(*pascal(i))
'''

def pascal(i) :
    lst = []
    for j in range(i):
        if j == 0 or j == i - 1:
            lst.append(1)
        else:
            lst.append(pascal(i-1)[j - 1] + pascal(i-1)[j])
    return lst

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    print(f'#{test_case}')
    for i in range(1, N+1):
        print(*pascal(i))