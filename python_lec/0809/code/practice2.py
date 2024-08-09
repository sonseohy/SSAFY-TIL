def f(i, k, s, t): # i: 원소, k: 집합의 크기, s: i-1까지 고려된 합, t: 목표
    global cnt
    global fcnt     # 함수의 호출 횟수
    fcnt += 1

    if s > t:   # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t:    # 남은 원소를 고려할 필요가 없는 경우
        cnt += 1
        return
    elif i == k:    # 모든 원소 고려
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t) # A[i] 포함
        bit[i] = 0
        f(i + 1, k, s, t)  # A[i] 미포함
'''
#가지치기 고려 X
    if i == k: # 모든 원소 고려했을 때
        if s == t:
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t) # A[i] 포함
        bit[i] = 0
        f(i + 1, k, s, t)  # A[i] 미포함

'''


N = 10
A = [i for i in range(1, N+1)] # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

key = 10
cnt = 0     # 합이 key와 같은 부분집합의 수
bit = [0] * N
fcnt = 0
f(0, N, 0, key)
print(cnt, fcnt)