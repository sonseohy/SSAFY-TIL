def hoare(left, right):
    p = arr[left]
    i = left+1
    j = right

    while i <= j:
        while i <= j and p >= arr[i]:   # 오답 : p > arr[i] 로 써서 (pivot보다 클 때만 i가 멈춰야되니까)
            i += 1
        while i <= j and p <= arr[j]:   # 오답 : p < arr[i] 로 써서 (pivot보다 작을 때만 j가 멈춰야되니까)
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]   # 14, 15줄을 while i<=j: 안에 써서 (i<=j일때 모두 swap진행 후 교차 되는 시점에서 pivot과 바꿔야 하니까)
    return j

def quick_sort(left, right):
    if left < right:
        pivot = hoare(left, right)
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, len(arr)-1)
    print(f'#{test_case} {arr[N//2]}')