# 0 1 1 2 3 5 8
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_m(n):
    if n <= 1 or memo[n]: # 이미 데이터가 있다면: (memo 0과 1은 이미 저장했으므로)
        return memo[n]  # 그 데이터를 호출
    memo[n] = fib_m(n-1) + fib_m(n-2)   # 없을때는 재귀호출해서 만들어서 저장
    return memo[n]

def fib_dp(n):
    dp = [0] * (n+1)        # 재귀 호출이 아니므로 dp를 밖에서 만들 필요 X
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

N = 5
print('재귀: ', fib(5))

N = 5
memo = [0] * (N + 1)
memo[0] = 0
memo[1] = 1
print('메모이제이션 : ', fib_m(N))

N = 5
print('dp : ', fib_dp(N))