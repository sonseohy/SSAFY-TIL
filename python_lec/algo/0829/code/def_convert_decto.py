# 정수를 입력받아 문자열 이진수를 return
def dectobin(value):
    strV = ''
    # while value > 0:
    for _ in range(8):
        strV = chr((value % 2) + ord('0')) + strV
        value = value // 2
    print(strV)
    return strV

def dectooct(value):
    strV = ''
    while value > 0:
        strV = chr((value % 8) + ord('0')) + strV
        value = value // 8
    print(strV)
    return strV

def dectohex(value):
    strV = ''
    while value > 0:
        if value % 16 < 10:
            strV = chr((value % 16) + ord('0')) + strV
        else:
            strV = chr((value % 16)-10 + ord('A')) + strV

        value = value // 16

    print(strV)
    return strV

i = 161
dectobin(i)
dectooct(i)
dectohex(i)
# b = bin(i)
