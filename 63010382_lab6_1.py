#Recursive 1
def func(arr, max_=None):
    if(max_ is None):
        max_ = arr.pop()
    current = arr.pop()
    if(current > max_):
        max_ = current
    if(arr):
        return func(arr, max_)
    return max_
def addnumber(number):
    if number==A:#จุดออก
        return number#จุดออก
    else:
        list3.append(int(inp[number]))
    number+=1#จุดวนซำ้
    addnumber(number)#จุดวนซำ้
inp=input("Enter Input : ").split()
list3=[]
A=len(inp)
#print(A)
addnumber(0)
#print(list3)
result = func(list3)
print("Max :",result)