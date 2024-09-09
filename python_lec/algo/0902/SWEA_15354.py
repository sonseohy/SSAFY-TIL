def course(x):
    global result
    if x == N-1:
        sum_cost = cost(path+[0])
        result = min(result, sum_cost)
        return
    
    for i in range(1, N):
        if used[i] == 1:
            continue
        path.append(i)
        used[i] = 1
        course(x+1)
        used[i] = 0
        path.pop()

def cost(lst):
    global result

    sum_v = 0
    for k in range(N):
        sum_v += BATTERY[lst[k]][lst[k+1]]
    
    return sum_v

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    BATTERY = [list(map(int, input().split())) for _ in range(N)]

    result = 10001
    path = [0]
    used = [0]*N
    course(0)

    print(f'#{test_case} {result}')