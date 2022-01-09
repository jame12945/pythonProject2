class LinkedList:
    class Node:
        def __init__(self, data, skip=None):
            self.data = data
            if skip is None:
                self.skip = None
            else:
                self.skip = skip

        def __str__(self):
            return str(self.data)

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.skip != None:
                t = t.skip
                self.size += 1
            self.tail = t

    def __str__(self):
        s = 'Linked data : '
        p = self.head
        while p != None:
            s += str(p.data) + ' '
            p = p.skip
        return s

    def __len__(self):
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.skip = p
            self.tail = p
        self.size += 1

    def removeHead(self):
        if self.head == None:
            return
        if self.head.skip == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.skip
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.skip
        return p


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.removeHead()
    def __str__(self):
        if not self.is_empty():
            out = 'Queue data : '
            for i in range(len(self.items)):
                val = self.items.nodeAt(i).data
                out += str(val) + ' '
            return out
        return 'Empty Queue'


    def __len__(self):
        return len(self.items)



inp = int(input('Enter choice : '))
if inp == 1:
        q1 = Queue()
        q1.enqueue(10)
        q1.enqueue(20)
        q1.enqueue(30)
        print(q1)
        q1.dequeue()
        q1.enqueue(40)
        print("Size of Queue :", len(q1))
        print(q1)
if inp == 2:
        q1 = Queue()
        q1.enqueue(100)
        q1.enqueue(200)
        q1.enqueue(300)
        q1.dequeue()
        print(q1)
        print("Queue is Empty :", q1.is_empty())
if inp == 3:
        q1 = Queue()
        q1.enqueue(11)
        q1.enqueue(22)
        q1.enqueue(33)
        q1.dequeue()
        q1.dequeue()
        q1.dequeue()
        print(q1)
        print("Size of Queue :", len(q1))
        print("Queue is Empty :", q1.is_empty())