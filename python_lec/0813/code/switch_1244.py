# answer
N = int(input())
switch = [-1] + list(map(int, input().split()))
num = int(input())
for _ in range(num):
    sex, no = map(int, input().split())

    # 남학생
    if sex == 1:
        for i in range(no, len(switch), no):
            switch[i] = (switch[i]+1) % 2

    # 여학생
    else:
        switch[no] = (switch[no] + 1) % 2
        start = no - 1
        end = no + 1
        while start >= 1 and end <= N and switch[start] == switch[end]:
            switch[start] = (switch[start]+1) % 2
            switch[end] = (switch[end] + 1) % 2
            start -= 1
            end += 1

for k in range(1, len(switch), 20):
    print(*switch[k:k+20])


# SWITCH_N = int(input())
# SWITCH = list(map(int, input().split()))
# STUDENT_N = int(input())
# arr = [list(map(int, input().split())) for _ in range(STUDENT_N)]
#
# for a in arr:
#     for i in range(SWITCH_N):
#         # 남자일 때
#         if a[0] == 1 and (i+1) % a[1] == 0:
#             if SWITCH[i]:
#                 SWITCH[i] = 0
#             else:
#                 SWITCH[i] = 1
#
#         # 여자일 때
#         elif a[0] == 2:
#             SWITCH[i] = (SWITCH[i] + 1) % 2
#             if (a[1]-1) - i >= 0 and (a[1]-1) + i < SWITCH_N :
#                 if SWITCH[(a[1]-1) - i] == SWITCH[(a[1]-1) + i]:
#                     start = (a[1] - 1) - i
#                     end = (a[1] - 1) + i
#             else:
#                 for j in range(start, end + 1):
#                     if SWITCH[j]:
#                         SWITCH[j] = 0
#                     else:
#                         SWITCH[j] = 1
#
# for k in range(SWITCH_N):
#     print(SWITCH[k], end=' ')
#     if (k+1) % 20 == 0:
#         print()