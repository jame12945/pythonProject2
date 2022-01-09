def fac(n):
    if n == 0:
        return 1
    else:
        return n + fac(n - 1)
def addnumber(number):
    if number==num:
        return
    print(str(number)+" + ",end='')
    number+=1
    addnumber(number)
print(" *** Natural sum ***")
num = int(input("Enter number : "))
addnumber(1)
print(str(num)+" ",end='')
print("= %d" % ( fac(num)-1))
