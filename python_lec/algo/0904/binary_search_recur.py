arr = [2, 4, 7, 9, 11, 19, 23]

def binary_search(low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if target == arr[mid]:
        return mid

    elif target < arr[mid]:
        return binary_search(low, mid - 1, target)
    else:
        return binary_search(mid + 1, high, target)