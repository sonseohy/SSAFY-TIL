def recur(x):
    if x == M:  # N개의 자연수 중 M개를 뽑기 위해
        print(*path)
        return

    for i in range(N):  # 후보군 : arr의 숫자 개수
        if used[i] == 1:
            continue

        path.append(arr[i])
        used[i] = 1
        recur(x+1)
        path.pop()
        used[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # 수열을 사전 순으로 증가하는 순서로 출력하기 위해 정렬

path = []
used = [0] * N
recur(0)