def hextobin(value):
    # 16진수를 10진수로
    decV = 0
    for c in value:
        if c.isdigit():
            decV = (decV * 16) + ord(c) - ord('0')
        else:
            decV = (decV * 16) + ord(c) - ord('A') + 10

    # 10진수를 2진수로
    binV = ''
    while decV > 0:
        binV = chr((decV % 2) + ord('0')) + binV
        decV //= 2

    if len(binV) % 4 != 0:
        while len(binV) % 4 != 0:
            binV = '0' + binV
    return binV

T = int(input())

for test_case in range(1, T+1):
    N, hexS = input().split()

    print(f'#{test_case} {hextobin(hexS)}')