MAX_SIZE = 100 
circular_queue = []
front = -1
rear = -1

def is_full(front, rear):
    if (rear + 1) % MAX_SIZE == front:
        return True
    else:
        return False


def enqueue(queue, front, rear, data):
    if is_full(front, rear) == True:
        print(f"\nQueue is full - {data} not added")
    else:
        rear = (rear + 1) % MAX_SIZE
        queue[rear] = data
        if front == -1: # First item to be queued
            front = 0
    return front, rear

def is_empty(front):
    if front == -1:
        return True
    else:
        return False


def dequeue(queue, front, rear):
    if is_empty(front) == True:
        print("\nQueue is empty - nothing to dequeue")
        dequeued_item = None
    else:
        dequeued_item = queue[front]
        # Check if the queue is empty
        if front == rear:
            front = -1
            rear = -1       
        else:
            front = (front + 1) % MAX_SIZE
            
    return dequeued_item, front, rear