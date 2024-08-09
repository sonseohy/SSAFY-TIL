TEST = 'abcdbcdabc'
PATTERN = 'cdb'

ip = jp = 0

while ip<len(TEST) and jp < len(PATTERN):
    if jp < len(PATTERN) and TEST[ip] == PATTERN[jp]:
            ip += 1
            jp += 1
    else:
        ip = ip-jp+1
        jp = 0

if jp == len(PATTERN):
    print(ip-jp)
else:
    print(-1)