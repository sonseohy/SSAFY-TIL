N = int(input())
nodes = list(map(int, input().split()))
delete = int(input())

count = 0
TREE = [[] for _ in range(N)]

for i in range(N):
    if nodes[i] != -1:
        TREE[nodes[i]].append(i)


# TREE.pop(delete)


for k in range(len(TREE)):
    if TREE[k] == []:
        count += 1

print(count)