n = int(input("Input : "))
print("",end='')
n2=n
if(n<0 or n==0):
    print("!!!Please enter number greater than zero!!!",end='')
elif (n > 0):
#upper
    print(" ")
    for i in range(1, n + 1):
        empt= 2 * n - 2 * i
        for j in range(i):
            print("*", end='')

        for j in range(empt):
            print(" ", end='')

        for j in range(i):
            print("*", end='')
        print("")
#lower
    for k in range(n2 - 1,0, -1):
        empt = 2 * n2 - 2 * k
        for z in range(k):
            print("*", end='')

        for z in range(empt):
            print(" ", end='')

        for z in range(k):
            print("*", end='')
        print("")
