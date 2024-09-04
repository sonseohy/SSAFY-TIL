# 중복순열
N = 6
K = 3

result = [0] * K
def recur(level):
    if level == K:
        print(result)
        return

    for i in range(1, N+1):
        result[level] = i
        recur(level+1)

recur(0)

# 순열
N = 6
K = 3
result = [0] * K
used = [False] * N
def recur(level):
    if level == K:
        print(result)
        return

    for i in range(1, N+1):
        result[level] = i
        recur(level+1)
