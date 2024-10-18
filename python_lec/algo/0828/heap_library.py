'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''

from heapq import heappush, heappop

N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

heap = []  # 최대힙을 구현하기 위한 리스트

# 최소힙 ( 기본 )
for num in arr:
    heappush(heap, num) # NlogN

print([x for x in heap])  # 힙의 내부 상태를 출력 (음수로 저장된 상태)

while heap:
    print(heappop(heap), end=' ')  # NlogN

print('\n------------------------------------')

# 최대힙
# 최대힙을 구할 때는 트릭이 필요 -> 라이브러리가 기본적으로 최소힙만 가능하도록 만들어져 있기 때문
# 삽입 시 음수로 곱하여 저장 (제일 큰 수가 제일 작아짐)
# 삭제 후 음수값을 곱하여 출력 (다시 원래 수로 복구하여 출력)
# 최대힙은 내가 저장하고 싶은 것을 음수로 곱해서 저장한다고 생각하면 됨
for num in arr:
    heappush(heap, -num)

print([-x for x in heap])  # 힙의 내부 상태를 출력 (음수로 저장된 상태)

while heap:
    print(-heappop(heap), end=' ')  # 