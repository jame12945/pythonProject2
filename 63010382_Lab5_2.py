class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dummy = Node(None)

    def __str__(self):
        if self.isEmpty():
            return ""
        self.head = self.dummy.next
        cur_head = self.head
        string = str(cur_head.data)
        while cur_head.next != None:
            # print(cur_head, cur_head.next)
            string += "->"
            string += str(cur_head.next.data)
            cur_head = cur_head.next
        return string

    def str_reverse(self):
        if self.isEmpty():
            return ""
        cur_tail = self.tail
        string = str(cur_tail.data)
        while cur_tail.previous != None:
            string += "->"
            string += str(cur_tail.previous.data)
            cur_tail = cur_tail.previous
        return string

    def isEmpty(self):
        return self.dummy.next == None

    def size(self):
        size = 0
        self.head = self.dummy
        temp_head = self.head
        while temp_head.next != None:
            temp_head = temp_head.next
            size += 1
        return size

    def append(self, data):
        new = Node(data)
        if self.dummy.next == None:
            self.dummy.next = new
            self.head = self.dummy.next
            return
        cur_head = self.head
        while cur_head.next != None:
            cur_head = cur_head.next
        cur_head.next = new

    def insert(self, index, data):
        if index > self.size() or index < 0:
            return "Data cannot be added"
        if self.dummy.next == None:
            new = Node(data)
            self.dummy.next = new
            self.head = self.dummy.next
            return "index = " + str(index) + " and data = " + str(data)

        else:
            new = Node(data)
            i = 0
            self.head = self.dummy
            cur_head = self.head
            while cur_head.next != None:
                if index == 0:
                    temp_head = cur_head.next
                    cur_head.next = new
                    cur_head.next.next = temp_head
                    return "index = " + str(index) + " and data = " + str(data)
                cur_head = cur_head.next
                i += 1
                if index == i:
                    # print("eoodf")
                    temp_head = cur_head.next
                    cur_head.next = new
                    cur_head.next.next = temp_head
                    # print(cur_head, cur_head.next)

            return "index = " + str(index) + " and data = " + str(data)

    def remove(self, data):
        index = 0
        self.head = self.dummy
        cur_head = self.head
        # print(cur_head)
        while cur_head.next != None:
            if cur_head.next.data == data:
                # print("remove should")
                cur_head.next = cur_head.next.next
                return "removed : " + str(data) + " from index : " + str(index)
            cur_head = cur_head.next
            index += 1
        return "Not Found!"

    def tail_set(self):
        self.head = self.dummy
        cur_head = self.head
        self.tail = None
        while cur_head.next != None:
            cur_head = cur_head.next
            pre_temp_tail = self.tail
            self.tail = cur_head
            self.tail.previous = pre_temp_tail


DLL = LinkedList()
input = input("Enter Input : ").split(",")
for x in input:
    if "A " in x:
        x = x.replace(" ", "")
        x = x.replace("A", "")
        DLL.append(x)
    elif "Ab" in x:
        x = x.replace(" ", "")
        x = x.replace("Ab", "")
        DLL.insert(0, x)
    elif "I" in x:
        # print("workkk")
        x = x.replace(" ", "")
        x = x.replace("I", "")
        index, data = x.split(":")
        # print(index,data)
        print(DLL.insert(int(index), data))
    elif "R" in x:
        x = x.replace(" ", "")
        x = x.replace("R", "")
        print(DLL.remove(x))
    DLL.tail_set()
    print("linked list :", DLL)
    print("reverse :", DLL.str_reverse())