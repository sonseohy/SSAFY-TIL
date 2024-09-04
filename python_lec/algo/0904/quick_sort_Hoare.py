def hoare_partition1(left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:    # i는 pivot보다 작거나 같으면 +1 (큰 값 탐색)
            i += 1
        while i <= j and arr[j] >= pivot:   # j는 크거나 같으면 -1 (작은 값 탐색)
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]