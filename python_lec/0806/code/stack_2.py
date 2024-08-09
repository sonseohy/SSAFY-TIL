def push(item):
    global top

    top += 1
    stack[top] = item

def pop():      # pop 할 때는 반드시 stack에 데이터가 있는지 확인해야 함
    global top

    result = stack[top]
    top -= 1
    return result

top = -1
N = 10
stack = [0] * N
push(3)
print(top, stack)
push(5)
print(top, stack)
push(1)
print(top, stack)

for _ in range(4):
    if len(stack) > 0: # or if (not쓰면 데이터가 없으면)stack: 리스트는 값이 하나도 없으면 False, 값이 있으면 True를 반환하기 때문
        item = pop()
        print(stack, item)

item = pop()
print(top, stack, item)
item = pop()
print(top, stack, item)
item = pop()
print(top, stack, item)

'''
pop을 한 후 stack에 값이 남아있긴 하지만 쓰레기 값
1 [3, 5, 1, 0, 0, 0, 0, 0, 0, 0] 1 # 유효한 데이터는 item 결과로 나온 인덱스 1까지, 즉 3, 5까지만 유효한 데이터
0 [3, 5, 1, 0, 0, 0, 0, 0, 0, 0] 5
-1 [3, 5, 1, 0, 0, 0, 0, 0, 0, 0] 3
'''

push(100)
print(top, stack)

# 다시 push 하면 값이 0번째에 들어가는 것을 확인할 수 있음



# 파이썬의 특성을 이용한 push, pop 함수
def push(item):
    stack.append(item)

def pop():
    return stack.pop() # pop(-1)

stack = []
push(3)
print(stack)
push(2)
print(stack)
push(1)
print(stack)

item = pop()
print(stack, item)
item = pop()
print(stack, item)
item = pop()
print(stack, item)

# 한번 더 pop 하면?
item = pop()
print(stack, item)
# 에러발생