SIZE = 3
queue = [-1] * SIZE
front = rear = -1

def isEmpty():
    return front == rear

def isFull():
    return rear == SIZE - 1

def enqueue(data):
    global rear
    if isFull():
        print('full')
        return -1

    rear += 1
    queue[rear] = data

def dequeue():
    global front
    if isEmpty():
        print('empty')
        return -1

    front += 1
    return queue[front]

enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
print(dequeue())
