def cal(v1, v2, op):
    if op == '+':
        return v2 + v1
    if op == '-':
        return v2 - v1
    if op == '*':
        return v2 * v1
    if op == '/':
        return v2 / v1

# 후위 표기식을 입력 받아 연산 결과를 return
def step2():
    stack = []
    for c in s:
        if c.isdigit():
            stack.append(int(c))    # stack에 문자열이 들어오면 계산이 어렵, 문자값과 숫자 값이 한 리스트에 들어가는 것도 좋지 않음 (다른 언어에서는 불가능 하기 때문) int로 받아옴
        else:   # 연산자인 경우
            value1 = stack.pop()
            value2 = stack.pop()
            stack.append(cal(value1, value2, c))


s = '65+28-2/+'
result = step2(s)

# s = '(6+5*(2-8)/2)'
# post_order = step1()
# print(step2(post_order))

print(result)