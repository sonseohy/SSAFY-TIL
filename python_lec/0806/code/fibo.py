def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    r1 = fibo(n-1)
    r2 = fibo(n-2)
    return r1 + r2

# 위 코드와 동일한 코드
def fibo(n):
    if n <= 1:
        return n

    return fibo(n-1) + fibo(n-2)

print(fibo(5))
print(fibo(6))