# 리스트의 왼쪽에 있는 데이타(pivot)를 최종 정렬 후
# 자기자리에 배치 시키고 그 위치를 return
# pivot을 기준으로 왼쪽에는 작은 값들, 오른쪽에는 큰값들을 배치
def partition_h(l, r):
    #arr = [6, 9, 5, 11, 1, 3, 13, 10]
    #      [6, 3, 5, 11, 1, 9, 13, 10]
    #      [6, 3, 5, 1, 11, 9, 13, 10]
    #      [1, 3, 5, 6, 11, 9, 13, 10]
    p = arr[l]
    i = l+1
    j = r
    while i<=j:
        while i<=j and arr[i] <= p: # 중복데이터의 정렬을 위해 arr[i] <= p (arr[i] < p는 오류 발생)
            i += 1
        while i<=j and arr[j] >= p: # 중복데이터의 정렬을 위해 arr[i] >= p (arr[i] > p는 오류 발생)
            j -= 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[l] = arr[l], arr[j]
    return j

def partition(l, r):
    p = arr[r]
    j = l-1 # 작은값과 큰값의 경계(마지막 작은 값의 위치)

    for i in range(l, r):
        # [1, 2, 5, 6, 10, 11, 12, 7, 8]: j:3, p:8, i:7
        if arr[i] < p:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
        # [1, 2, 5, 6, 7, 10, 11, 12, 8]: j:4
    arr[j+1], arr[r] = arr[r], arr[j+1]
    return j+1


    # [6, 9, 5, 11, 1, 3, 13, 10]

def quick_sort(l, r):
    if l < r:
        p = partition(l, r)
        quick_sort(l, p-1)
        quick_sort(p+1, r)

arr = [6, 9, 5, 1, 3, 13, 10]
# [1, 3, 5, 6, 9, 10, 13]
N = len(arr)

quick_sort(0, N-1)
print(arr)