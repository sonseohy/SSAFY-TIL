# s 문자열에 있는 중위 표기를 후위 표기로 바꿔서 return
def step1():
    icp = {'(':3, '+':1, '-':1, '*':2, '/':2}  # 연산자 우선순위를 설정
    isp = {'(':0, '+': 1, '-': 1, '*': 2, '/': 2}  # stack 안에서의 연산자 우선순위 설정
    stack =[]
    result = ''
    for c in s:
        if c.isdigit():
            result += c
        elif c == ')':
            while stack and stack[-1] != '(':   # stack이 비어있지 않을 때 진행해야 하므로 stack == True 조건 추가
                result += stack.pop()
            stack.pop()     # 남아있는 왼쪽 괄호도 pop해서 버림
        else:
            if stack and isp[stack[-1]] >= icp[c]:
                result += stack.pop()
            stack.append(c)

    while stack:    # stack에 연산자가 남아있을 때
        result += stack.pop()

    return result


s = '(6+5*(2-8)/2)'
post_order = step1()
print(post_order)