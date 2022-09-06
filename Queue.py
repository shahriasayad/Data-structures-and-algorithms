
class Queue:
    def __init__(self,size_of):
        self.items = [0]*size_of
        self.max_size = size_of
        self.size = 0
        self.head = 0
        self.tail = 0

    def enqueue(self,item):
        if self.is_full():
            print("queue is full")
            return
        print("inserting item :",item)
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size = self.size + 1

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False

    def is_empty(self):
        if self.size == 0:
            return  True
        else:
            return False

if __name__ =="__main__":
    pass
