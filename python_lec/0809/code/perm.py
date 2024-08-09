def construct_cand(k):   # 후보 숫자 정하는 함수
    candidates = []
    for i in range(N):
        if i not in c[:k]:
            candidates.append(i)
    return candidates

# 부분집합의 합 함수로 뺀 것
def subset_sum():
    sumV = 0
    for i in range(N):
        if c[i] == 1:
            sumV += numbers[i]
    print(sumV)

# k번째에 1 or 0
def permu(k):
    if k == N:
        #print(c) # 부분집합 인덱스
        for i in c:
            print(numbers[i], end=' ')
        print()
        return

    candidates = construct_cand(k) # 후보만들 때 앞에 쓰여진 숫자는 쓰지 않기 위해 k를 인자로 보내줌
    for i in candidates:
        c[k] = i
        permu(k+1)
    return # return이 숨어있음


N = 3
numbers = [12, 2, 5]
c = [-1] * N    # 디버깅 편의를 위해 0이 아닌 -1로 생성
permu(0)