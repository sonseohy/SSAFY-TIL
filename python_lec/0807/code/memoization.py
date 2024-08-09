def fibo1(n):
    # global memo # 생략해도 문제는 없음
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

# memo 사용하지 않고 재귀로 계산하는 함수
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


n = 900
memo = [0] * (n + 1)
memo[0] = 0
memo[1] = 1
print(fibo1(n))
print(fibo(n))

# fibo1은 시간복잡도가 n이기 때문에 n이 900일때 값이 출력되지만
# fibo는 시간복잡도가 2^n이기 때문에 n이 900일 때 값이 출력되지 않음
# 효율 차이가 많이남