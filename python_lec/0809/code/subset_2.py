def construct_cand():   # 후보 숫자 정하는 함수
    return [0, 1]

# 부분집합의 합 함수로 뺀 것
def subset_sum():
    sumV = 0
    for i in range(N):
        if c[i] == 1:
            sumV += numbers[i]
    print(sumV)

# k번째에 1 or 0
def powerset(k):
    if k == N:
        print(c)
        # subset_sum() # 함수로 따로 썼을 때
        # 부분집합의 합 구하기
        sumV = 0
        for i in range(N):
            if c[i] == 1:
                sumV += numbers[i]
        print(sumV)
        return
    c[k] = 0
    powerset(k+1)
    c[k] = 1
    powerset(k+1)

    # 위의 코드와 같은 의미
    candidates = construct_cand()
    for i in candidates:
        c[k] = i
        powerset(k+1)


N = 3
numbers = [12, 2, 5]
c = [-1] * N    # 디버깅 편의를 위해 0이 아닌 -1로 생성
powerset(0)