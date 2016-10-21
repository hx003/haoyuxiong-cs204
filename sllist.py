class ListNode:
    def __init__(self, data = None):
        '''
        initialize the node
        '''
        self.data = [data]
        self.next = None
    def __getitem__(self):
        return self.data

class sllist:
    def __init__(self):
        '''
        initialize a list with size = 0
        '''
        self.size = 0
        self.head = None
        self.stack = SStack()
        
    def __len__(self):
        # length of the list is its size
        return self.size     

    def insert(self, item):
        '''
        insert a node with given item to the given index
        if the index is greater than the current size of the list
        insert to the last
        '''
        curnode = self.head

    def insert(self, item, index):
        '''
        insert the node with input item at the input index
        '''
        
        if index>=self.size-1:
            index = self.size
        elif index <=0:
            index = 0
        newnode = ListNode()
        newnode.data = [item]
        if index == 0:
            nextnode = self.head
            self.head= newnode
            self.head.next = nextnode
            self.size += 1
        elif index != 0:
            curnode = self.head
            nextnode = curnode.next
            index-=1
            while index > 0 and nextnode!= None:
                curnode = nextnode
                nextnode = curnode.next
                index-=1
            curnode.next = newnode
            newnode.next = nextnode
            self.size+=1

    def insertdata(self, item):
        if self.head == None:
            self.append(item)
            return
        else:
            cur = self.head
            nex = cur.next
            while cur.data[0] != item and nex != None:
                cur = nex
                nex = cur.next
            cur.data[1]+= 1
        

    def add(self, item):
        '''
        append an item to the first of the list
        '''
        if self.stack.isEmpty():
                
            newNode = ListNode(item)
            newNode.data += [1]
        else:
            newNode = self.stack.pop()
            
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
        '''
        pop a node with given index and return its value
        if index is none, pop the last node
        '''
        current = self.head
        previous = None
        if not self.stack.isEmpty():
            return self.stack.pop()
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
        '''
        give the index of a node
        return its value
        '''
        if not self.stack.isEmpty():
            return self.stack.top()
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
        '''
        when the runner is not none
        return the value of the node
        '''
        if self.runner == None:
            raise StopIteration
        else:
            item = self.runner.data
            self.runner = self.runner.next
            return item
    def __iter__(self):
        return self




class SStack:
    def __init__(self):
        self.head = None
        self.__size = 0
    def push(self, item, value):
        newnode = Node(item)
        newnode.data += [value]
        newnode.next = self.head
        self.head = newnode
        self.__size += 1
        
    
    def pop(self):
        if self.head == None:
            return
        current = self.head
        self.head = current.next
        self.__size-=1
        return current.data
    
    def isEmpty(self):
        return self.__size == 0

    def top(self):
        if self.__size == 0:
            return None
        else:
            return self.head.data


    
    
