SIZE = 4
queue = [-1] * SIZE
front = rear = 0

def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % SIZE == front

def enqueue(data):
    global rear
    if isFull():
        print('full')
        return -1

    rear = (rear+1) % SIZE
    queue[rear] = data

def dequeue():
    global front
    if isEmpty():
        print('empty')
        return -1

    front = (front+1) % SIZE
    return queue[front]

enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
print(dequeue())
enqueue(4)
print(queue, front, rear)