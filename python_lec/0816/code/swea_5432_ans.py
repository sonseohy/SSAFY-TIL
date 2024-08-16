T = int(input())

for tc in range(1, T+1):
    arr = input()
    total = 0
    cnt = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            cnt += 1
        elif arr[i] == ')':
            cnt -= 1
            if arr