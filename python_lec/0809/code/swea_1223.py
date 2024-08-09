def cal_sum(v1, v2, op):
    if op == '+':
        return v2 + v1
    if op == '*':
        return v2 * v1

def cal(s):
    stack = []

    for c in s:
        if c.isdigit():
            stack.append(int(c))
        else:
            value1 = stack.pop()
            value2 = stack.pop()
            stack.append(cal_sum(value1, value2, c))

    return stack.pop()

def postfix():
    stack = []
    result = ''
    icp = {'+':1, '*':2}

    for c in s:
        if c.isdigit():
            result += c
        else:
            if stack and icp[stack[-1]] >= icp[c]:
                result += stack.pop()
            stack.append(c)

    while stack:
        result += stack.pop()

    s_sum = cal(result)
    return s_sum

T = 1

for test_case in range(1, T + 1):
    N = int(input())
    s = input()

    print(f'#{test_case} {postfix()}')

