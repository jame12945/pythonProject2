def search(lst,x):
    if x > max(lst):
        return "No First Greater Value"
    else:
        min = 10000000000
        index = -1
        for i in range(0,len(lst)):
            if min > lst[i] - x > 0:
                min = lst[i] - x
                index = i
        return lst[index]

input, value = input("Enter Input : ").split('/')
input = list(map(int,input.split()))
num = list(map(int,value.split()))

for i in num:
    print(search(input,i))