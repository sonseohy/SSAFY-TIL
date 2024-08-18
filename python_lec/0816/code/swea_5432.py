T = int(input())

for test_case in range(1, T+1):
    s = input()

    # 레이저의 위치를 찾아 저장할 stack 생성
    laser_stack = []
    r = 0
    for i in range(len(s)):
        if laser_stack and laser_stack[-1] == '(' and s[i] == ')':
            laser_stack.pop()
            laser_stack.append('o')
            r += 1
        else:
            laser_stack.append(s[i])
    print(*laser_stack)

    stack = []
    cnt = 0
    result = 0
    while laser_stack:
        t = laser_stack.pop()
        if t == ')':
            stack.append(t)
        elif stack and laser_stack and t == 'o':
            tmp = 0
            stack.append(t)
            if laser_stack[-1] == '(':
                cnt += 1
                if stack and stack[-1] == 'o':
                    while stack and stack[-1] == 'o':
                        stack.pop()
                        tmp += 1
                        cnt += 1
                result += cnt
                stack.pop()
                laser_stack.pop()
                if stack:
                    for _ in range(tmp):
                        stack.append('o')
                    cnt = 0
            elif laser_stack[-1] == 'o':
                continue

        elif stack and t == '(':
            cnt += 1
            tmp = 0
            if stack and stack[-1] == 'o':
                while stack and stack[-1] == 'o':
                    stack.pop()
                    tmp += 1
                    cnt += 1
            result += cnt
            if stack:
                for _ in range(tmp):
                    stack.append('o')
            cnt = 0

        if stack == []:
            cnt = 0

    print(f'#{test_case} {result}')



# # 제한시간 초과 발생

# T = int(input())

# for test_case in range(1, T+1):
#     s = input()

#     # 레이저의 위치를 찾아 저장할 stack 생성
#     laser_stack = []
#     r = 0
#     for i in range(len(s)):
#         if laser_stack and laser_stack[-1] == '(' and s[i] == ')':
#             laser_stack.pop()
#             laser_stack.append('o')
#             r += 1
#         else:
#             laser_stack.append(s[i])
#     print(*laser_stack)

#     stack = []
#     cnt = 0
#     result = 0
#     while laser_stack:
#         t = laser_stack.pop()
#         if t == ')':
#             stack.append(t)
#         elif stack and laser_stack and t == 'o':
#             tmp = 0
#             stack.append(t)
#             if laser_stack[-1] == '(':
#                 cnt += 1
#                 if stack and stack[-1] == 'o':
#                     while stack and stack[-1] == 'o':
#                         stack.pop()
#                         tmp += 1
#                         cnt += 1
#                 result += cnt
#                 stack.pop()
#                 laser_stack.pop()
#                 if stack:
#                     for _ in range(tmp):
#                         stack.append('o')
#                     cnt = 0
#             elif laser_stack[-1] == 'o':
#                 continue
#             # elif laser_stack[-1] == ')':
#             #     cnt = 0
#         elif stack and t == '(':
#             cnt += 1
#             tmp = 0
#             if stack and stack[-1] == 'o':
#                 while stack and stack[-1] == 'o':
#                     stack.pop()
#                     tmp += 1
#                     cnt += 1
#             result += cnt
#             if stack:
#                 for _ in range(tmp):
#                     stack.append('o')
#             cnt = 0

#         if stack == []:
#             cnt = 0

#     print(f'#{test_case} {result}')
# ((()())(())()))
# (((1 2)(3) 4))
#
#     3    2
#         5
#         5



