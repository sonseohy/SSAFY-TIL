N = int(input())
nodes = list(map(int, input().split()))
delete = int(input())

count = 0
TREE = [[] for _ in range(N)]

for i in range(N):
    if nodes[i] != -1:
        TREE[nodes[i]].append(i)
print(TREE)
for t in range(N):
    for idx in range(len(TREE[t])):
        TREE[t].append()

print(TREE)

for k in range(len(TREE)):
    if TREE[k] == []:
        count += 1

print(count)