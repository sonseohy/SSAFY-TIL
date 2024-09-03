arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def visit_cafe(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt

result = 0
for tar in range(0, 1 << n):
    if visit_cafe(tar) >= 2:
        result += 1
print(result)


abc
abd
abe
bcd
bce
cde