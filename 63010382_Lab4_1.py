class Queue:
    def __init__(self,list=None):
        if(list==None):
           self.items=[]
        else:
            self.items=list
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self, i):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    #we want empty queue
    #แล้วก็แลงstringเป็นเลขปรกติ
    #เขียนเคสดักตรงemptyจบ

q1=Queue()
q2=Queue()
'''print(q1.items)
q1.enQueue('A')
q1.enQueue('B')
'''
str=input("Enter Input : ").split(",")

for i in str :
    if "E" in i:
     q1.enQueue(i[2:len(i)])#q1.items=[1,2,3]
     #change list to numberhere
     lst2=q1.items

     join = ', '.join(q1.items)
     print(join)
     #to here
     #print(f"{q1.items}")
    else :
      if(q1.size()!=0):
        print(f"{q1.items[0]} <- ",end='')
        q2.enQueue(q1.items[0])
        q1.deQueue(0)
        # change list to numberhere
        if(q1.size()!=0):
            join = ', '.join(q1.items)
            print(join)
        else:
            print("Empty")
        # to here
      else:
        print("Empty")
  # change list to numberhere
if(q2.size()==0):
    q2.enQueue("Empty")
join2 = ', '.join(q2.items)
join3 = ', '.join(q1.items)
if(q1.size()!=0):
 print(f"{join2} : {join3}")
else:
  join3="Empty"
  print(f"{join2} : {join3}")

