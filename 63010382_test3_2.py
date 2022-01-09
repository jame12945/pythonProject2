def Minimum(num):
    if len(num) == 1:
        return num[0]
    elif(len(num)!=1):
        minimum = num [ 0 ]
        minNum = Minimum(num[ 1:len(num)])

        if minNum< minimum:
            minimum = minNum
        else:
            None
        return minimum
        return max(num[0], Minimum(num[ 1:len(num) ]))
        return findMaximum(num [ 1:len(num) ]) if findMaximum(num [ 1: len(num) ]) < num [ 0 ] else num [ 0 ]


input = list(map(int, input('Enter Input : ').split()))
implement=input
print("Min :", Minimum(implement))