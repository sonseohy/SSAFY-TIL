arr = [2, 4, 7, 9, 11, 19, 23]  # 정렬된 데이터

def binary_search(target):
    low = 0
    high = len(arr) - 1
    
    cnt = 0 # 탐색 횟수
    
    while low <= high:
        mid = (low + high) // 2
        cnt += 1
        
        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target: # 왼쪽을 확인해야 한다 (target값이 작으면)
            high = mid - 1
        else:
            low = mid + 1   # 오른쪽을 확인해야한다 (target값이 크면)
    
    return -1, cnt # 못 찾았을 경우