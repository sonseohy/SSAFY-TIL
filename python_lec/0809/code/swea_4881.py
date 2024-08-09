def construct_cand(k):
    candidates = []
    for i in range(N):
        if i not in c[:k]:
            candidates.append(i)
    return candidates

def permu(k):
    if k == N:
        for i in range(len(c)):
            print(arr[i][c[i]], end=' ')
        print()
        return

    candidates = construct_cand(k)
    for i in candidates:
        c[k] = i
        permu(k+1)
    return

T = int(input())

for test_case in range(1, T + 1):
     N = int(input())
     arr = [list(map(int, input().split())) for _ in range(N)]

     c = [-1] * N
     (permu(0))
