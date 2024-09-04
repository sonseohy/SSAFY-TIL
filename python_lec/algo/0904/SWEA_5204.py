def merge_sort(lst):
    if len(lst) == 1:
        return lst

    m = len(lst)//2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

    return merge(left, right)

def merge(left, right):
    global cnt

    result = [0] * (len(left) + len(right))
    l_idx = 0
    r_idx = 0

    if left[len(left)-1] > right[len(right)-1]:
        cnt += 1

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            result[l_idx+r_idx] = left[l_idx]
            l_idx += 1
        else:
            result[l_idx+r_idx] = right[r_idx]
            r_idx += 1

    while l_idx < len(left):
        result[l_idx+r_idx] = left[l_idx]
        l_idx += 1

    while r_idx < len(right):
        result[l_idx+r_idx] = right[r_idx]
        r_idx += 1

    return result


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    merge_lst = merge_sort(arr)
    print(f'#{test_case} {merge_lst[N//2]} {cnt}')