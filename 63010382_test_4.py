x= int(input("Enter a positive number : "))


if(x>0 and x<=15):
    count1 = 1
    count2 = 1
    count3 = 1

    for i in range(1, x +1):

        if i == 1:
            for j in range(1, x +1):
                print("%X" % count1, end=" ")
                count1 += 1

        if i == x:

            for j in range(1, x+1 ):
                if j == 1:
                    print("%X" % count1, end=" ")
                elif(j!=1):
                    print("%X" % count2, end=" ")
                    count2 += 1
        if(i!=1 and i != x):

            for j in range(1, x+1 ):
                if j == 1:
                    print("%X" % count1, end=" ")
                elif j == x:
                    print("%X" % count3, end=" ")
                    count3 += 1

                elif(j!=1 or j!=x):
                    print(" ", end=" ")

        print("")
        count1 = i + 1
if x > 15:
    print(x, "is too high.")


if x <= 0:
    print(x, "is too low.")
