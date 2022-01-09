c = 0
def push(list, n):
    if n == 0:
        return list
    else:
        global c
        list = push(list, n-1)

        last = n

        lN = list[last]

        c += 1
        list, position = shamble(list, n, last, lN)

    return list

def shamble(list, x, last, lN):
    global c
    if x < 0:
        return list, last

    if x>= 0:
        list, position = shamble(list, x-1, last, lN)

        if list[last] < list[x]:
            if list[last] == lN:

                position = x

            temp = list[last]
            list[last] = list[x]
            list[x] = temp
            if x != 0:
                c += 1
        return list, position


print(' *** Insertion sort ***')
inp = [int(i) for i in input('Enter some numbers : ').split()]

a = len(inp)-1

list = push(inp,a)
print()
print(list)
print('Data comparison = ', c)