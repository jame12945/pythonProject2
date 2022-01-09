def maxIndex(a, index, n):
    if index == n:
        return index
    k = maxIndex(a, index + 1, n)
    return (index if int(a [ index ]) < int(a [ k ]) else k)


def sort(lst, n, index=0):
    if index == n:
        return -1
    k = maxIndex(lst, index, n - 1)
    if k != index:
        lst [ k ], lst [ index ] = int(lst [ index ]), int(lst [ k ])
    else:
        lst [ index ] = int(lst [ index ])
    sort(lst, n, index + 1)


def Med(lst):
    long = len(lst) - 1
    sort(lst, len(lst))
    if (long + 1) % 2 == 0 and long + 1 > 2:
        x = int(long / 2)
        return (lst [ x ] + lst [ x + 1 ]) / 2
    elif (long + 1) % 2 == 1 and long + 1 > 1:
        x = int((long + 1) / 2)
        return float(lst [ x ])
    elif long + 1 == 1:
        x = lst [ 0 ]
        return float(x)
    else:
        return (lst [ 0 ] + lst [ 1 ]) / 2


def output(l, index, lst=[ ], output_lst=[ ]):
    if index == 0:
        lst.append(l [ index ])
        output_lst.append(l [ index ])
        print('list = {lst} : median = {med}'.format(lst=output_lst, med=Med(lst)))
        return 0
    output(l, index - 1, lst, output_lst)
    lst.append(l [ index ])
    output_lst.append(l [ index ])
    print('list = {lst} : median = {med}'.format(lst=output_lst, med=Med(lst)))


l = [ e for e in input("Enter Input : ").split() ]
if l [ 0 ] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    l = list(map(int, l))
    output(l, len(l) - 1)
