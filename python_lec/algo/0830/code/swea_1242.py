# 암호코드는 총 8개의 숫자 : 앞 7자리 = 고유번호, 마지막 자리 = 검증 코드
# (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드가 10의 배수
# 배열은 16진수로 이루어져있고, 2진수로 변환해 확인해야함
# 배열에는 1개 이상의 암호코드가 존재, 모든 암호코드가 정상적인 암호코드 x
# 암호코드의 정상여부 확인 후 숫자들의 합 출력
# 각 숫자 하나가 차지하는 최소 칸수는 7

def hextobin(hexS):
    intV = 0
    for c in hexS:
        if c.isdigit():
            intV = (intV * 16) + ord(c) - ord('0')
        else:
            intV = (intV * 16) + ord(c) - ord('A') + 10

    value = ''
    while intV > 0:
        value = chr((intV % 2) + ord('0')) + value
        intV = intV // 2

    if len(value) % 4 != 0:
        while len(value) % 4 != 0:
            value = '0' + value
    return value

def decoding(c):
    s = ''
    for k in c:
        if k == '0':
            s += k
        else:
            s += hextobin(k)

    i = len(s)-1
    while i >= 0:
        if s[i] == '1':
            print(s[i-55:i+1])
            i -= 56
            continue
        i -= 1

    # bin_code = []
    #
    # print(bin_n)
    # print(len(bin_n))
    # for i in range(len(bin_n)-1, -1, -1):
    #     if bin_n[i] == '1':
    #         print(i)
    #         s = bin_n[:i]
    #         break

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    NUMBERS = [input() for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if NUMBERS[r][c] != '0':
                code = decoding(NUMBERS[r])
                break
