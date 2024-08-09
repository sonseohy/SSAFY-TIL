# 1
stack = []

stack.append(1) # push(1)
stack.append(2) # push(2)
stack.append(3) # push(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())

# 2
STACK_SIZE = 10
stack = [0] * STACK_SIZE
top = -1

# push(1)
top += 1
stack[top] = 1
# push(2)
top += 1
stack[top] = 2
# push(3)
top += 1
stack[top] = 3

# pop()
# 방법 1
top -= 1
print(stack[top+1])

# 방법 2
print(stack[top])
top -= 1

