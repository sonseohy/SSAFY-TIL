# 2. 0.5로 계산하는 방법 (check 필요)
def dectobin(N):
    strV = ''
    for i in range(1, 13):
        N -= 0.5 ** i
        if N >= 0:  # 0 이상이면
            strV += '1'  # strV에 1 추가
            if N == 0:  # 0이 되면 strV 리턴
                return strV

        else:    # 0 이하이면
            strV += '0'  # strV에 0 추가 후
            N += 0.5 ** i  # 이전 상태로 복구

    return 'overflow'  # 13자리 이상은 'overflow' 리턴


"""
# 1. 소수를 2진수로 변환하는 방법 사용 : 소수에 2 곱한 후 소수점 앞자리 체크
def dectobin(value):
    binV = ''

    while value != 1.0:
        value *= 2
        binV += str(int(value))
        if value > 1:
            value -= 1

    if len(binV) > 12:
        return 'overflow'
    return binV

T = int(input())

for test_case in range(1, T+1):
    N = float(input())

    print(f'#{test_case} {dectobin(N)}')
"""