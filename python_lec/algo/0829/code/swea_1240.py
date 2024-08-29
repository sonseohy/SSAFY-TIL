# 암호코드는 8개의 숫자
# 암호코드에서의 숫자 하나는 7개의 비트로 암호화되어 주어짐
# (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수
def decode(num):
    lst = []
    s = ''
    for i in range(M-1, -1, -1):
        if num[i] == '1':
            s = num[i-55:i+1]
            break

    for j in range(0, len(s), 7):
        lst.append(code_lst[s[j:j+7]])

    odd_sum = even_sum = 0
    for k in range(8):
        if k % 2 == 0:
            odd_sum += lst[k]
        else:
            even_sum += lst[k]

    if ((odd_sum*3) + even_sum) % 10 == 0:
        return sum(lst)
    else:
        return 0

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    NUMBERS = [input() for _ in range(N)]
    code_lst = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
              }

    for n in range(N):
        for m in range(M):
            if NUMBERS[n][m] == '1':
                code = NUMBERS[n]
                break

    print(f'#{test_case} {decode(code)}')
