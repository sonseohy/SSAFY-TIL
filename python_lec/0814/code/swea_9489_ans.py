T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로축
    maxV = 0
    for r in range(N):
        cnt = 0
        for c in range(M):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if maxV < cnt:
                    maxV = cnt
                cnt = 0
        if maxV < cnt:
            maxV = cnt

    # 세로축
    for c in range(M):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if maxV < cnt:
                    maxV = cnt
                cnt = 0
        if maxV < cnt:
            maxV = cnt

    print(f'#{tc} {maxV}')


'''
arr2 = list(zip(*arr))
# 가로와 세로 길이가 같을 때 가로와 세로를 바꿔서 가로와 똑같은 체크를 해주어 값 구할 수 있음
# 가로축 구하는 반복문을 함수로 빼고 리스트만 arr, arr2로 넣어주어 최대값 구하기 가능
'''
'''
def rowCheck(a):
    pass
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
rowCheck(arr)

arr2 = list(zip(*arr))
rowCheck(arr2)

print(f'#{tc} {maxV}')
'''