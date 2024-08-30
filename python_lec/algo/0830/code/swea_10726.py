def dectobin(value):
    bin_V = ''
    if value == 0:
        return '0'

    while value > 0:
        bin_V = chr((value%2)+ord('0')) + bin_V
        value //= 2

    return bin_V

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    bin_M = dectobin(M)

    result = ''
    # N보다 bin_M 길이가 짧다면 앞에 0으로 채우기 (오답! 0으로 안채우고 하다보면 일부 tc에서 막힘)
    if len(bin_M) < N:
        bin_M = '0' * (N-len(bin_M)) + bin_M

    for i in range(N):
        if bin_M[len(bin_M)-1-i] == '1':
            result = 'ON'
        else:
            result = 'OFF'
            break

    print(f'#{test_case} {result}')
