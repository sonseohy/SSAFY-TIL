T = int(input())

for test_case in range(1, T + 1):
    S = input()

    stack = []

    for i in S:
        if stack and stack[-1] == i:
            item = stack.pop()
        else:
            stack.append(i)
        print(stack)

    print(len(stack))