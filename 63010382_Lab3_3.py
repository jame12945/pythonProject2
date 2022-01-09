class Stack():
    ### Enter Your Code Here ###

    # return s.pop()
    def __init__(self,):
        self.list=[]
    def push(self, i):
        self.list.append(i)
    def pop(self):
        if len(self.list)>0 :
            return self.list.pop()
        else:
            print("empty list")
    def isEmpty(self):
        return len(self.list)==0
    def size(self):
       return len(self.list)

def postFixeval():
    print(" ***Postfix expression calcuation***")

    token = input("Enter Postfix expression : ").split()


    s = Stack()
    for i in token:
         if i in ("+","-","*","/"):
            op1,op2=s.pop(),s.pop()#3=op1,2=op2
            if i == '+':
                s.push(op2+op1)#[5]
            elif i == '-':
                 s.push(op2 - op1)
            elif i == '*':
                 s.push(op2 * op1)
            elif i == '/':
                s.push(op2 / op1)
         else:
             s.push(int(i))#23+
         #print(s.list)

    if not s.isEmpty():
        print("Answer : ", '{:.2f}'.format(s.pop()))
    else:
        print("empty list")


postFixeval()



