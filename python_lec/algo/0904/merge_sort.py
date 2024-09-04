def merge_sort(m):
    if len(m) == 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)   # 두 개의 정렬된 리스트를 병합하여 반환

def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0 # 왼쪽, 오른쪽 리스트의 0번 리스트부터 비교하기 위해 l, r 인덱스 0으로 설정 -> 비교 후 result 리스트에 담음

    while l <len(left) and r < len(right):  # 왼쪽 리스트, 오른쪽 리스트 다 볼 때까지
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):    # 비교가 끝나고 왼쪽 리스트만 남았다면
        result[l+r] = left[l]
        l += 1

    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result

