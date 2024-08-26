class LinearQueue():
    def _init__(self,max_size):
        self.MAX_SIZE = max_size
        self.queue = [None]*self.MAX_SIZE
        self.front = 0
        self.rear = -1
    
    def enqueue(self,data):
        if self.is_full():
            print("full")
        else:
            self.rear+=1
            self.queue[self.rear]=data
    
    def is_full(self):
        if self.rear+1==self.MAX_SIZE:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.is_empty():
            print("empty")
            dequed_item=None
        else:
            dequed_item=self.queue[self.front]
            self.front+=1
            return dequed_item
    
    def is_empty(self):
        if self.front>self.rear:
            return True
        else:
            return False