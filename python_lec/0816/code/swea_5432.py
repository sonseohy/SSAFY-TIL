T = int(input())

for test_case in range(1, T+1):
    s = input()
    # #
    # r = 0
    # idx = []
    # for i in range(1, len(s)):
    #     if s[i-1] == '(' and s[i] == ')':
    #         r += 1
    # stick = (len(s) - r * 2) // 2

    stack = []
    r = 0
    for i in range(len(s)):
        if stack and stack[-1] == '(' and s[i] == ')':
            stack.pop()
            stack.append('o')
            r += 1
        else:
            stack.append(s[i])
    print(*stack)



# ((()())(())()))
# (((1 2)(3) 4))
#
#     3    2
#         5
#         5



