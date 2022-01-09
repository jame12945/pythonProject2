class Queue:
    def __init__(self,list=None):
        if(list==None):
           self.items=[]
        else:
            self.items=list
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    def size(self):
         return len(self.items)

qstr=Queue()#['k', 'q', 'u', 'w', 'm', 'S', 'a', 'y', 'n', 'p', 'v']
qnum=Queue()#256183
qaskii=Queue()
qans=Queue()
qlist=Queue()
qtest=Queue()
Input,num =input("Enter String and Code : ").split(",")
count=0
count2=0
list=""
dlist=""
listans=""
dnum=""
n=1
n2=1
j=0
loop =0
for i in Input:
    if (i !=" "):
        qstr.enQueue(i)
        count +=1
strsize=qstr.size()
#print(strsize)
for i in num:
    if (i !=" "):
        qnum.enQueue(i)
        count2 +=1
       # qlist.enQueue(i)
        qtest.enQueue(i)

#print(qtest.items)
numsize=qnum.size()

while(loop<=strsize):#0<9
        if(loop==numsize):
            j=0
        else:
            x2=qtest.deQueue()
            qlist.enQueue(x2)
            qtest.enQueue(x2)
            j+=1
            #print(loop)
        loop+=1
#print(qlist.items)#use this

#print(numsize)
while (n <= count):

    list=qstr.deQueue()
    qstr.enQueue(list)
    qaskii.enQueue(ord(list))
    """
        """
    n += 1
n=1
#print(qaskii.items)
while (n2<=qstr.size()):
        n2+=1
        dlist = qaskii.deQueue()
        qaskii.enQueue(dlist)
        dnum = qnum.deQueue()
        qnum.enQueue(dnum)
        dnum2=qlist.deQueue()
        qlist.enQueue(dnum2)
        x=int(dnum2)
        y=dlist+x
       # print(y)
        if (y > 122 ):
                    y-=26
                    #print(y)
                    qans.enQueue(chr(y))

        elif(y>90 and y<97 ):
            y-=26
            qans.enQueue(chr(y))

        else:
                 #print(y)
                 qans.enQueue(chr(y))
n2=1
print("Encode message is :  ",end='')
print(qans.items)
print("Decode message is :  ",end='')
print(qstr.items)