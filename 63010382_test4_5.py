c = 0
def mergesort(x):
    global c
    if len(x) > 1:
        Right = len(x)//2
        Left = x[:Right]
        Median = x[Right:]

        mergesort(Left)
        mergesort(Median)

        i =0
        j =0
        k = 0

        while i < len(Left) and j < len(Median):
            if Left[i] < Median[j]:
                x[k] = Left[i]
                i += 1
            else:
                x[k] = Median[j]
                j += 1
            k += 1
            c += 1

        while i < len(Left):
            x[k] = Left[i]
            i += 1
            k += 1

        while j < len(Median):
            x[k] = Median[j]
            j += 1
            k += 1

def listout(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()



print(" *** Merge sort ***")
inp = list(map(int,input("Enter some numbers : ").split()))
mergesort(inp)
print("\nSorted -> ",end='')
listout(inp)
print("Data comparison = ", c)