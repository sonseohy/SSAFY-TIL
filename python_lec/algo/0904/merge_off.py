def merge_sort(lst):
    if len(lst) == 1:
        return lst

    m = len(lst) // 2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

    return merge(left, right)   # 두 개의 정렬된 리스트를 병합하여 반환

def merge(left, right):
    lidx = 0
    ridx = 0

    result = []
    while lidx <len(left) and ridx < len(right):
        if left[lidx] < right[ridx]:
            result.append(left[lidx])
            lidx += 1
        else:
            result.append(right[ridx])
            ridx += 1

    # 비교가 끝나고 남은 리스트가 있다면 result 뒤에 붙이기
    result += left[lidx:]
    result += right[ridx:]

    return result

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print(merge_sort(arr))

"""

# lst를 입력 받아 정렬후 결과 리스트를 return
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    m = len(lst) // 2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])
    return merge(left, right)

#두개의 list를 입력 받아서 하나의 리스트로 변합 결과를 return
def merge(left, right):
    lidx = 0
    ridx = 0

    result = []
    while lidx<len(left) and ridx<len(right):
        if left[lidx] < right[ridx]:
            result.append(left[lidx])
            lidx += 1
        else:
            result.append(right[ridx])
            ridx += 1

    result += left[lidx:]
    result += right[ridx:]
    return result

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print(merge_sort(arr))

"""