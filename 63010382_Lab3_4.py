class Stack :

    def __init__(self,list=None) :
        if list == None:
            self.list = []
        else:
            self.list = list

    def isEmpty(self) :
        return len(self.list) == 0

    def push(self,data) :
        self.list.append(data)

    def pop(self) :
        if self.isEmpty():
            return None
        else:
            return self.list.pop()

    def size(self) :
        return len(self.list)

    def peek(self) :
        return self.list[-1]



def infix2postfix() :
    s = Stack()
    result = ''
    op = set(['+','-','*','/','(',')'])
    priority = {'':0,'+':1,'-':1,'*':2,'/':2}#ตั้งค่าความสำคัญ
    print(" ***Infix to Postfix***")
    token = input("Enter Infix expression : ")

    for i in token:
        if i not in op:
            result += i#ใส่abcได้ว่าabcd
        elif i == '(':
            s.push('(')#ในs จะเท่ากับ('(')
        elif i == ')':
            while s.size() and s.peek() != '(':
                result += s.pop()#s.pop=list[(,(,(,-]
            s.pop()#ถ้าไม่ใช่while popออก
        else:#ถ้าเป็น+-*/ทำงานต่อจากif
            while s.size() and s.peek() != '(' and priority [i] <= priority [s.peek()]:
                result += s.pop()
            s.push(i)#ถ้าไม่ใช่while pushเข้า
    while not s.isEmpty():
        result += s.pop()

    print("PostFix :"+'\n'+result)

infix2postfix()
