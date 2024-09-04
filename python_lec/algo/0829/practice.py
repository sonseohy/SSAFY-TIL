def bintodec(s):
    intV = 0

    for c in s:
        intV = (intV * 2) + ord(c) - ord('0')

    return intV

s = '0000000111100000011000000111100110000110000111100111100111111001100111'
for i in range(0, len(s), 7):
    binS = s[i:i+7]

    print(bintodec(binS))