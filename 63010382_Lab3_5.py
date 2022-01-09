"""
class Stack:

    def __init__(self, list=None):
        if list == None:
            self.item = [ ]
        else:
            self.item = list
    def isEmpty(self):
        return len(self.item) == 0
    def push(self, i):
        self.item.append(i)
    def pop(self):
        if len(self.item) > 0:
            return self.item.pop()

    def size(self):
        return len(self.item)
    def peek(self):
        if len(self.item) == 0:
            print("kuy")
        return self.item [ -1 ]
class realStack:

    def __init__(self, list=None):
        if list == None:
            self.item = [ ]
        else:
            self.item = list
    def isEmpty(self):
        return len(self.item) == 0
    def push(self, i):
        self.item.append(i)
    def pop(self):
        if len(self.item) > 0:
            return self.item.pop()
    def size(self):
        return len(self.item)
    def peek(self):
        if len(self.item) == 0:
            print("kuy")
        return self.item [ -1 ]

list1=[]
list2=[]
s=Stack()
realStack1 = realStack()
str=input("Enter Input : ").split(",")
for i in str:
    list1.append([x for x in i.split()])
for i in list1:
    if i[0]=='A':
        s.push(i[1])
        realStack1.push(i[1])
    if i[0]=='B':
        if (s.size() == 0):
            print(s.size())
        else:
            list2.append(s.pop())#'3'
        for i2 in range(len(s.item)):#4
            if int(s.item[-1]) > int(list2[-1]) :#4>3
                list2.append(s.pop())  # '3,4' มองเห็น
            else:
                s.pop()#มองไม่เห็นต้นข้างหลัง
        for i3 in  range(len(list2)) :
             s.push(list2.pop())
             print(s.size())
    if i[0]=="S":#4 3 จะกลายเป็น 3 5
         for j in range(len(s.item)):
             s.pop()
         for f in range(len(realStack1.item)):
             list2.append(int(realStack1.pop()))
         for k in range(len(list2)):
             if list2 [ -1 ] % 2 == 0:
                 x = int(list2.pop()) - 1
                 if (x < 1):
                     x = 1
                 s.push(x)
                 realStack1.push(x)
                 # print(S.items,"--->even number -1")
             else:
                 x = int(list2.pop()) + 2
                 s.push(x)
                 realStack1.push(x)

"""

class Stack:
    def __init__(self,list = None):
        if list == None:
         self.items=[]
        else:
         self.items = list
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def size(self) :
        return len(self.items)
    def num(self):
        return int(len(self.items))
class realStack:
    def __init__(self,list = None):
        if list == None:
         self.items=[]
        else:
         self.items = list
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def size(self) :
        return len(self.items)
    def num(self):
        return int(len(self.items))
lst_input = []
lst_decoy = []
S = Stack()
rs = realStack()
input_list = input("Enter Input : ").split(",")
for e in input_list:
  lst_input.append([i for i in e.split()])

for i in lst_input:
    if i[0] == 'A':
        S.push(i[1])

        rs.push(i[1])
    if i[0] == 'B':
        if(S.size() == 0):
            print(S.size())
        else:
         lst_decoy.append(S.pop())

         for j in range(len(S.items)):
            if int(S.items[-1]) > int(lst_decoy[-1]):
                lst_decoy.append(S.pop())

            else:
                S.pop()

         for j in range(len(lst_decoy)):
                S.push(lst_decoy.pop())

         print(S.size())
    if i[0] == 'S':
        for j in range(len(S.items)):
            S.pop()
        for f in range(len(rs.items)):
            lst_decoy.append(int(rs.pop()))
        for k in range(len(lst_decoy)):
            if lst_decoy[-1]%2 == 0:
                x = int(lst_decoy.pop())-1
                if(x < 1):
                    x = 1
                S.push(x)
                rs.push(x)

            else:
                x = int(lst_decoy.pop())+2
                S.push(x)
                rs.push(x)

