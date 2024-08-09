# T = int(input())
#
# for test_case in range(1, T + 1):
#     A, B = input().split()
#
#     a = len(A)
#     b = len(B)
#
#     cnt = 0
#
#     for i in range(a - b + 1):
#         for j in range(b):
#             if A[i + j] != B[j]:
#                 break
#             else:
#                 cnt += 1
#
#     print(cnt)
#     print(f'#{test_case} {a - (b * cnt) + cnt}')

T = int(input())

for test_case in range(1, T + 1):
    A, B = input().split()

    a = len(A)
    b = len(B)

    cnt = 0

    i = 0
    j = 0
    while j < b and i < a:
        if A[i] != B[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == b:
            cnt += 1
            j = 0

    print(f'#{test_case} {a - (b * cnt) + cnt}')

# j = 0을 생략하면 문자를 한 번 찾고 while문이 끝나서 제대로 카운트 되지 않음

