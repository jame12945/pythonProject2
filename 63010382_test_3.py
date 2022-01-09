
n=input("Enter number end with (-1) : ").split()
list=[]
list2=[]
list3=[]
list4=[]
count=0
y=0
x=0

#print(list)
if"-1" in n:
    for i in n:
        if"-1"not in i:
           list2.append(i[0:len(i)])

           if i not in list3:
               list3.append(i)
           count+=1

        else:
           count-=1
           break
    #count
    for x in list3:
        a = 0
        if x in list2:
           a =list2.count(x)
        list4.append(a)
    found=False
    for x in list4:
        index=list4.index(x)
        if x>len(list2)/2 :
            print(list3[index])
            found=True
    if(found==False):
        print("kuy")
   # print(list2)
    #print(list3)
    #print(list4)
else:
    print("Invalid INPUT !!!")


#print(count)
