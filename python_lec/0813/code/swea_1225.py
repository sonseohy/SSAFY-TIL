T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    front = 0
    rear = 8

    check = True
    zero_idx = 0
    while check:
        for i in range(1, 6):
            front = (front + 1) % 9
            num = arr[front] - i
            if num <= 0:
                num = 0
                rear = (rear + 1) % 9
                arr[rear] = num
                zero_idx = rear
                check = False
                break
            rear = (rear + 1) % 9
            arr[rear] = num
    print(f'#{test_case}', end=' ')
    for i in range(8):
        print(arr[(zero_idx + 2 + i) % 9], end=' ')
    print()