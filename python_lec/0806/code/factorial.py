def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))

#
def f(n):
    global cnt
    cnt += 1
    if n == 0:
        return
    else:
        f(n-1)

cnt = 0
f(1000)
print(cnt)
