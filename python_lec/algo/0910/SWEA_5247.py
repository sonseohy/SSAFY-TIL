import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
# 연산의 중간 결과도 항상 백만 이하의 자연수여야 함
def bfs(value):
    cnt = 0
    q = []
    visited = [False] * 1000001

    q.append(value)
    visited[value] = True

    while q:
        value = q.popleft()
        if value == M:
            return cnt

        for value in [value*2, value-10, value+1, value-1]:
            if 0 < value <= 1000000 and not visited[value]:
                q.append(value, cnt+1)
                visited[value] = True

    return cnt



T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{test_case} {bfs(N)}')






# # dfs : 시간초과
# def dfs(n, cnt):
#     global result
#     if n == M:
#         result = min(result, cnt)
#         return
#
#     if n > M or cnt > result:
#         return
#
#     for i in [n+1, n-1, n*2, n-10]:
#         if i > 0:
#             dfs(i, cnt+1)
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#
#     result = 1000000
#     dfs(N, 0)
#     print(f'#{test_case} {result}')