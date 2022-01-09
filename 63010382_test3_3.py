def palindome01(inp,x):
    global y
    if y < x:
        if inp[y] == inp[(-1-y)*1]:
            y += 1
            return palindome01(inp,x)
        if inp [ y ] != inp [ (-1 - y) * 1 ]:

             return 'is not palindrome'
    else:
        return 'is palindrome'
def check(a):
    global x
    global y
    if y < len(a):
        if a[y].isalpha() == True:
            x.append(a[y].lower())
        y += 1
        return check(a)
    if y >= len(a):
        y = 0
        return x




x = []
y= 0
input = input('Enter Input : ')
check(input)
print("'" + input + "'", end=" ")
print(palindome01(x, int(len(x) / 2)))

#Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era