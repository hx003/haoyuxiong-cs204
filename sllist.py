class ListNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __getitem__(self):
        return self.data

class sllist:
    def __init__(self):
        self.size = 0
        self.head = None
        
    def __len__(self):
        return self.size     

    def insert(self, item, index):
        current = self.head
        previous = None
        newNode = ListNode(item)
        if index < self.size:
            if index == 0:
                self.head = newNode
                newNode.next = current
            else:
                for x in range(index):
                    if current.next == None:
                        break
                    previous = current
                    current = current.next 
                newNode.next = current
                previous.next = newNode
        else:
            while current.next != None:
                current = current.next
            current.next = newNode
            newNode.next = None
                
        self.size += 1

    def append(self, item):
        newNode = ListNode(item)
        if self.size == 0:
            self.head = newNode
            newNode.next = None
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
            newNode.next = None
        self.size += 1

    def pop(self, index = None):
        current = self.head
        previous = None
        if index == None:
            if self.size == 1:
                self.head = None
            else: 
                while current.next!= None:
                    previous = current
                    current = current.next
                previous.next = None
                self.size -= 1
            return current.data
            
        if index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                for x in range(index):
                    previous = current
                    current = current.next
                previous.next = current.next
            self.size -= 1
            return current.data

    def peek(self, index):
        if index >= self.size:
            raise ListException
        else:
            current = self.head
            for x in range(index):
                current = current.next
            return current.data

    def __iter__(self):
        return _ListIterator(self.head)


        
class _ListIterator:
    def __init__(self, head):
        self.runner = head
    def __next__(self):
        if self.runner == None:
            raise StopIteration
        else:
            item = self.runner.data
            self.runner = self.runner.next
            return item
    def __iter__(self):
        return self

    
