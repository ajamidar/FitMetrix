MAX_SIZE=100
queue=[None]*MAX_SIZE
front=0
rear=-1

def enqueue(data):
    global rear
    if is_full():
        print("full")
    else:
        rear=rear+1
        queue[rear]=data

def is_full():
    global rear
    global MAX_SIZE
    if rear+1==MAX_SIZE:
        return True
    else:
        return False

def dequeue():
    global front
    if is_empty():
        print("empty")
        dequeued_item=None
    else:
        dequed_item=queue[front]
        front=front+1
        return dequed_item

def is_empty():
    if front>rear:
        return True
    else:
        return False
