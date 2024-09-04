def bintodec(binS):
    intV = 0
    for b in binS:
        intV = (intV*2) + ord(b) - ord('0')
    return intV

def trittodec(tritS):
    intV = 0
    for t in tritS:
        intV = (intV*3) + ord(t) - ord('0')
    return intV

T = int(input())

for test_case in range(1, T+1):
    bin_num = list(input())
    trit = list(input())

    result = 0
    for i in range(len(bin_num)):
        bin_num[i] = str((int(bin_num[i])+1) % 2)
        binV = bintodec(''.join(bin_num))
        for j in range(len(trit)):
            trit[j] = str((int(trit[j]) + 1) % 3)
            tritV = trittodec(''.join(trit))
            if binV == tritV:
                result = binV
                break
            else:
                trit[j] = str((int(trit[j]) + 1) % 3)
                tritV = trittodec(''.join(trit))
            if binV == tritV:
                result = binV
                break
            trit[j] = str((int(trit[j]) + 1) % 3)
        if result != 0:
            break
        bin_num[i] = str((int(bin_num[i]) + 1) % 2)

    print(f'#{test_case} {result}')
