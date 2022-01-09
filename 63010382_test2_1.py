class Stack:

    def __init__(self, list=None):
        self.Data = 0
        if list == None:
            self.item = [ ]
        else:
            self.item = list

    def push(self, Data):
        self.item.append(Data)

    def pop(self):
        if len(self.item) > 0:
            return self.item.pop()
        else:
            print("empty list")

    def size(self):
        return len(self.item)

    def is_empty(self):
        return len(self.item) == 0


    def peek(self):
        if not self.is_empty():
            y=-1
            return self.item [ y ]
        return None
    def __str__(self):
        if not self.is_empty():
            output = "Data in Stack is : "
            for stk_data in self.item:
                output += str(stk_data) + ' '
            return output
        return 'This Empty'
    def bottom(self):
        if not self.is_empty():
            x=0
            return self.item [ x]
        return None


s1 = Stack()
input = int(input("Enter choice : "))
if input == 1:
     s1 = Stack()
     s1.push(10)
     s1.push(20)
     print(s1)
     s1.pop()
     s1.push(30)
     print("Peek of stack :", s1.peek())
     print("Bottom of stack :", s1.bottom())
if input == 2:
        s1 = Stack()
        s1.push(100)
        s1.push(200)
        s1.push(300)
        s1.pop()
        print(s1)
        print("Stack is Empty :", s1.is_empty())
if input == 3:
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :", s1.size())