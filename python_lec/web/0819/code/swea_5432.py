T = int(input())

for test_case in range(1, T + 1):
    s = input()

    cut = 0
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            cut += 1
        if s[i] == ')':
            cut -= 1
            if s[i-1] == '(':
                result += cut
            else:
                result += 1
    print(f'#{test_case} {result}')