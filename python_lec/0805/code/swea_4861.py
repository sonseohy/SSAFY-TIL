# def row_palindrome(arr):
#     # 가로 회문
#     for a in arr:
#         palindrome = ''
#         for i in range(M):
#             if a[i] == a[N - 1 - i]:
#                 palindrome += a[i]
#                 result = 1
#             else:
#                 result = 0
#                 break
#         if result == 1:
#             return palindrome
#
# def col_palindrome(arr):
#     # 세로 회문
#     for i in range(N):
#         palindrome = ''
#         for j in range(M):
#             if arr[j][i] == arr[N - 1 - j][i]:
#                 palindrome += arr[j][i]
#                 result = 1
#             else:
#                 result = 0
#                 break
#         if result == 1:
#             return palindrome
#
# def palindrome(N, M):
#     i = 0
#     j = 0
#     palindrome = ''
#     while j < M and i < N:
#         if arr[i] != arr[M-j-1]:
#             i = i - j
#             j = -1
#         i += 1
#         j += 1
#         palindrome += arr[i][j]
#     if j == M:
#         return palindrome
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]
#
#     result = ''
#     if N == M:
#         if row_palindrome(arr):
#             result = row_palindrome(arr)
#         elif col_palindrome(arr):
#             result = col_palindrome(arr)
#     else:
#         result = palindrome(N, M)
#
#     print(f'#{test_case} {result}')
'''
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    palindrome = ''
    for a in arr:
        start = 0
        for i in range(N-M+1):
            for j in range(M):
                if a[j] != a[j - 1 - i]:
                    break
                else:
                    palindrome += a[j]

    print(palindrome)
'''


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    palindrome = ''
    for a in arr:
        i = 0
        j = 0
        for k in range(N - M + 1):
            while j < M and i < N:
                if arr[k + i] != [k + M - 1 + j]:
                    i = i - j
                    j = -1
                    palindrome = ''
                i += 1
                j += 1
                palindrome += arr[k + i][k + M - 1 + j]

    print(palindrome)