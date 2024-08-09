def permu(k):
    if k == N:
        print(c)
        return

    for i in range(N):
        # i가 위에서 사용중이면 continue
        if used[i]:
            continue
        # 사용중이 아니면
        # 사용하지 않았으면 사용중으로 만들고 내려감
        c[k] = i
        used[i] = True
        permu(k+1)
        used[i] = False # 내려갔다가 다시 올라오면 사용하지 않았다고 표시 (다음번째 칸의 체크를 위해)

N = 14
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [-1] * N
used = [False] * N
permu(0)