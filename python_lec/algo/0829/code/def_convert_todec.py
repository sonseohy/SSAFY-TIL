# 문자열 진수 표현을 입력 받아 10진수 정수를 return
def bintodec(binS):
    intV = 0
    for c in binS:
        intV = (intV*2) + ord(c) - ord('0')
    print(intV)
    return intV

def octtodec(octS):
    intV = 0
    for c in octS:
        intV = (intV*8) + ord(c) - ord('0')
    print(intV)
    return intV

def hextodec(hexS):
    intV = 0
    for c in hexS:
        if c.isdigit():
            intV = (intV*16) + ord(c) - ord('0')
        else:
            intV = (intV*16) + ord(c) - ord('A') + 10

    print(intV)
    return intV

i = '101'
bintodec(i)
octtodec(i)
i = 'AB'
hextodec(i)