# 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
# 단, 순서에 따른 중복을 제거하세요
arr = [i for i in range(1, 11)]
path = []


# 버전1
# idx : 파라미터로 후보군 없애주기
def dfs(level, sum, idx):   # idx 의미 : 현재 수보다 작은 수들은 이미 고려가 되었음
    # 가지치기 : 합이 10이면 종료
    if sum == 10:   # 기저 조건 : 문제에서 발견하기 힘든 경우가 많다.
        print(*path)
        return

    # 가지치기 : 10이상의 숫자면 볼 필요 없음
    if sum > 10:
        return

    for i in range(idx, len(arr)):  # idx보다 작은 후보들은 pass
        # 가지치기 : 이미 사용한 숫자라면 생략
        if arr[i] in path:
            continue

        path.append(arr[i])
        dfs(level + 1, sum + arr[i], i)
        path.pop()


# 버전2
# 1을 썼으면 앞으로는 1을 고려하지 않아도 되는 경우 이진 트리 구조처럼(True or False) 풀이가 가능하다.
# 트리 구조처럼 사용하면 훨씬 쉽고 빠르다
# 이진 트리처럼 사용 (후보를 사용하느냐 vs 마느냐) 하면 훨씬 쉽고 빠르다
def dfs2(level, sum):
    if sum > 10:
        return

    if sum == 10:
        print(*path)
        return

    # 모두 선택하지 않으면 합이 10이 넘지 못하므로 (아무것도 고르지 않을 때 주의해서 처리, 반례를 잘 생각해야 함(다 False라면?))
    # 기저조건 추가
    if level == len(arr):
        return

    # 선택하는 경우
    path.append(arr[level]) # 경로 저장용
    dfs2(level + 1, sum + arr[level])
    path.pop()

    # 현재 숫자를 선택하지 않는 경우
    dfs2(level + 1, sum)


# dfs(0, 0, 0)
dfs2(0, 0)