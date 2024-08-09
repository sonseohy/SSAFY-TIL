# 경사값과 길이를 구해서 이전까지의 최소값과 비교하며 결과를 return 한다.
def getValue(s, e):
    global res_value, res_len
    maxV = # s와 e 사이에서 제일 큰 값
    minV = # s와 e 사이에서 제일 작은 값

    value = # 경사값
    l = e - s + 1

    if res_value > value:
        res_value = value
        res_len = l
    elif res_value == value:

    return res_value, res_len # global 변수이므로 return 값 안해줘도 됨

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    start = end = 0
    res_value = 101 # 경사값
    res_len = 0 # 길이
    for end in range(start, N - 1):
        if arr[end] <= arr[end+1]:
            continue
        else:
            res_value, res_len = getValue(start, end)
            start = end + 1

    if arr[-1] >= arr[-2]:
        end += 1
    else:
        end = start # 이 문제에서는 else문의 코드 필요 없음

    if end - start >= 1:
        res_value, res_len = getValue(start, end)

    print(f'#{tc} {res_len}')


