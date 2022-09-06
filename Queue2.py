
class queue:
    def __init__(self):
        self.items =[]

    def is_empty(self):
        if self.items ==[]:
            return True
        return False

    def _enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

if __name__ =="__main__":
    obj = queue()
    obj._enqueue(44)
    obj._enqueue(23)
    obj._enqueue(222)

    while not obj.is_empty():
        item = obj.dequeue()
        print(item)




