N = 10
q = [0] * N

front = -1
rear = -1

# enqueue(1)
rear += 1
q[rear] = 1
# enqueue(2)
rear += 1
q[rear] = 2
# enqueue(3)
rear += 1
q[rear] = 3

# dequeue()
front += 1
print(q[front])
front += 1
print(q[front])
front += 1
print(q[front])

# 다른 방법
# but. append, pop은 시간이 오래걸림
q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))
print(q2.pop(0))