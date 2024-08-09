# s의 () 짝이 맞으면 True, 아니면 False return
def isPait(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False # 오른쪽 괄호가 남은 경우
            stack.pop()
    if stack:
        return False # 왼쪽 괄호가 남은 경우

    return True

s = '(()()(())(()))'
print(isPait(s))
s = '((()))))())'
print(isPait(s))
s = '((('
print(isPait(s))
s = ')))'
print(isPait(s))