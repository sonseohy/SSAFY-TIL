T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split())) + [0]
    front = -1
    rear = N - 1

    i = 0
    result = 0
    while i < M:
        front = (front + 1) % (N + 1)
        rear = (rear + 1) % (N + 1)
        arr[rear] = arr[front]
        result = arr[(i+1)%(N+1)]

        i += 1

    print(f'#{test_case} {result}')
