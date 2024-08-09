def is_pair(a):
    stack = []
    for s in a:
        if s == '(' or s == '{':
            stack.append(s)
        if s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif s == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0

    if stack:
        return 0
    return 1


T = int(input())
top = -1

for test_case in range(1, T + 1):
    arr = input()

    result = is_pair(arr)

    print(f'#{test_case} {result}')

# 오답 정리
# (} 의 경우 올바른 짝이 아님
# ( 일때 앞의 요소가 ) , { 일때 앞의 요소가 } 여야 올바른 괄호 짝
# peek과 같이 스택의 마지막 요소를 보고 싶을땐 stack[-1]
