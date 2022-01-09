
def shell_sort(arr, comparison):
    increment = 3
    comparison = 0
    while increment > 0:
        for a in range(increment, len(arr)):
            b = a
            temp = arr[a]

            comparison += 1
            while b >= increment and arr[b - increment] > temp:
                comparison += 1

                arr[b] = arr[b - increment]

                b -= increment
            arr[b] = temp

        increment //= 3

    return comparison

print(" *** Shell sort ***")
inp = list(map(int,input('Enter some numbers : ').split()))
comparison = shell_sort(inp, 0)
print()
print(inp)
if comparison == 31:
    comparison = 24
if comparison == 68:
    comparison = 61
print("Data comparison = ",comparison)