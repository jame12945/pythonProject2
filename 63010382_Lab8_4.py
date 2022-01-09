pow, merge = input("Enter Input : ").split("/")
merge= merge.split(",")
pow = list(map(int, pow.split()))
n = len(pow)
print(sum(pow))
for i in merge:
    a = int(i [ 0 ])
    b = int(i [ 2 ])
    P1 = pow [ a ]
    P2 = pow [ b ]
    if a * 2 + 1 < n:
        if a * 2 + 2 < n:
            P1 += pow[ a * 2 + 2 ]
        P1 += pow [ a * 2 + 1 ]
    if b * 2 + 1 < n:
        if b * 2 + 2 < n:
            P2 += pow [ b * 2 + 2 ]
        P2 += pow [ b * 2 + 1 ]
    if (P1 > P2):
        print(str(a) + ">" + str(b))
    if (P1 == P2):
        print(str(a) + "=" + str(b))
    if(P1 < P2):
        print(str(a) + "<" + str(b))