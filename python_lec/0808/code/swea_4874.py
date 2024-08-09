def cal(v1, v2, op):
    if op == '+':
        return v2 + v1
    if op == '-':
        return v2 - v1
    if op == '*':
        return v2 * v1
    if op == '/':
        return v2 // v1 # v2 / v1으로 써서 error 발생

def postfix(s):
    stack = []
    for c in s:
        if c.isdigit():
            stack.append(int(c))
        elif c == '.':
            if len(stack) != 1:
                return 'error'
            return stack.pop()
        else:
            if len(stack) > 1:
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(cal(value1, value2, c))
            else:
                return 'error'
    return 'error' # return 없어도 상관 X, 그전에 다 걸림

T = int(input())

for test_case in range(1, T + 1):
    s = list(input().split())

    print(f'#{test_case} {postfix(s)}')
