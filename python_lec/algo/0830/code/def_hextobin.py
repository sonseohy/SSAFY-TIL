def hextobin(c):
    if c.isdigit():
        value = int(c)
    else:
        value = ord(c) - ord('A') + 10

    result = ''
    for i in range(4):
        if (value >> i) & 1:
            result = '1' + result
        else:
            result = '0' + result

    return result

def bintodec(s):
    value = 0
    for c in s:
        value = value*2 + int(c)
    return value
