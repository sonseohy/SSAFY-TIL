import sys
sys.stdin = open('input.txt', 'r')

'''
마이너스 반례
1
3
0 1 0 1
3 5 3
'''

def cal(n1, n2, op_idx):
    if op_idx == 0: # 덧셈
        return n1 + n2
    if op_idx == 1: # 뺄셈
        return n1 - n2
    if op_idx == 2: # 곱셈
        return n1 * n2
    if op_idx == 3: # 나눗셈
        if n1 < 0:
            return -(abs(n1) // n2)
        return n1 // n2

# 재귀 설계
# 시작점 : 첫 번째 숫자
# 끝점 : 모든 수(연산자)를 사용할 때까지
# 파라미터 : 특정 시점에서 계산된 결과값
def bfs(level, total):
    global min_result, max_result

    if level == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    # 4개의 연산자를 확인
    for i in range(4):
        if operator[i] == 0:    # 남은 연산자가 없으면 통과
            continue

        operator[i] -= 1
        bfs(level+1, cal(total, numbers[level], i))
        operator[i] += 1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_result = 1e9
    max_result = -1e9

    bfs(1, numbers[0])
    print(f'#{test_case} {max_result - min_result}')