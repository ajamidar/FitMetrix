class CircularQueue():
    def __init__(self,max_size):
        self.MAX_SIZE = max_size
        self.circular_queue = []
        self.front = -1
        self.rear = -1

    def is_full(self):
        if (self.rear + 1) % self.MAX_SIZE == self.front:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.is_full(self.front, self.rear) == True:
            print(f"\nQueue is full - {data} not added")
        else:
            self.rear = (self.rear + 1) % self.MAX_SIZE
            self.circular_queue[self.rear] = data
            if self.front == -1: # First item to be queued
                self.front = 0
        return self.front, self.rear
    
    def is_empty(self):
        if self.front == -1:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.is_empty(self.front) == True:
            print("\nQueue is empty - nothing to dequeue")
            self.dequeued_item = None
        else:
            self.dequeued_item = self.circular_queue[self.front]
            # Check if the queue is empty
            if self.front == self.rear:
                self.front = -1
                self.rear = -1       
            else:
                self.front = (self.front + 1) % self.MAX_SIZE
                
        return self.dequeued_item, self.front, self.rear   