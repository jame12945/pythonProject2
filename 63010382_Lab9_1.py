list = [int(i) for i in input('Enter Input : ').split()]
for loop in range(1, len(list)):
    moveNum = None
    swap = False

    for i in range(len(list) - loop):
        if list[i] > list[i + 1]:
            moveNum = list[i]
            list[i], list[i + 1] = list[i + 1], list[i]
            swap = True

    if loop <= len(list) - 1 and swap is False:
        print('last step :', list, f'move[{moveNum}]')
        break
    elif loop == len(list) - 1:
        print('last step :', list, f'move[{moveNum}]')
    else:
        print(f'{loop} step :', list, f'move[{moveNum}]')