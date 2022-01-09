s1 = []
s2 = []
s3= []


def goinout(start, dest):
    global s1
    global s2
    global s3
    if start == 'A':
        x = s1.pop(0)
    elif start == 'B':
        x = s2.pop(0)
    else:
        x = s3.pop(0)
    if dest == 'A':
        s1.insert(0, x)
    elif dest == 'B':
        s2.insert(0, x)
    else:
        s3.insert(0, x)
    # print(a, b, c)


def appear(maxn, row):
    global s1
    global s2
    global s3
    acp = s1[::-1]
    bcp = s2[::-1]
    ccp = s3[::-1]
    if row == 0:
        return
    if row == maxn:
        print('|  |  |')
    if len(s1) >= row:
        print(f"{acp[row-1]}  ", end="")
    else:
        print('|  ', end="")
    if len(s2) >= row:
        print(f"{bcp[row-1]}  ", end="")
    else:
        print('|  ', end="")
    if len(s3) >= row:
        print(f"{ccp[row-1]}", end="")
    else:
        print('|', end="")
    if row != 0:
        print()
    appear(maxn, row-1)




def move(n, start, filler, dest, maxn):
    if n == 1:
        print(f"move {n} from  {start} to {dest}")
        goinout(start, dest)
        appear(maxn, maxn)
    else:
        move(n-1, start, dest, filler, maxn)
        print(f"move {n} from  {start} to {dest}")
        goinout(start, dest)
        appear(maxn, maxn)
        move(n-1, filler, start, dest, maxn)


def rec_init_a(num, target):
    global s1
    if num <= target:
        s1.append(num)
        rec_init_a(num+1, target)


if __name__ == '__main__':
    n = int(input("Enter Input : "))
    rec_init_a(1, n)
    appear(n, n)
    move(n, 'A', 'B', 'C', n)