class LinkedList:
    class Node :
        def __init__(self,item,next = None) :
            self.item = item
            if next is None :
                self.next = None
            else :
                self.next = next

        def __str__(self) :
            return str(self.item)
    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.item)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size

    def append(self, item):
        p = self.Node(item)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail =p
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.item

    def isEmpty(self) :
        return self.size == 0

    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def removeDup(self):
        if not self.isEmpty():
            memmory = {}
            previus = None
            buf1 = self.head
            while buf1 is not None:
                if memmory.get(buf1.item,0) == 0:
                    memmory[buf1.item] = 1
                    previus = buf1
                    buf1 = buf1.next
                else:
                    if buf1.next is not None:
                        previus.next = buf1.next
                        buf1.next = None
                        buf1 = previus.next
                    else:
                        previus.next = None
                        buf1 = None

inputlist = [int(e) for e in input('Enter numbers : ').split()]

link= LinkedList()
for item in inputlist:
    link.append(item)
print("Linkedlist Before removeDuplicate")
print(link)
print("Linkedlist After removeDuplicate")
link.removeDup()
print(link)