def Insertion(inp,  answer, cur):
    if len(inp) == 0:
        print("\nsorted")
        return

    if len( answer) == 0:
        answer.append(inp.pop(0))
        Insertion(inp, answer, 0)
    else:
        if cur < len( answer) and inp[0] >  answer[cur]:
            Insertion(inp,  answer, cur+1)
        else:

            temp = inp.pop(0)
            answer.insert(cur, temp)
            print("insert {0} at index {1} :".format(temp, cur), end=" ")
            print( answer, end=" ")
            if inp:
                print(inp)
            Insertion(inp,  answer, 0)
    return  answer

inp = list(map(int, input("Enter Input : ").split()))
n = len(inp)
a = list()
# print(inp)
print(Insertion(inp, a, 0))