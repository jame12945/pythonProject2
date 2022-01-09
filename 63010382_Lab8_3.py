n, input = input("Enter Input : ").split("/")
n = int(n)

input = input.split()
input = list(map(int, input))

if (n+1)//2 >= len(input):
    i = 0
    while len(input) < n:
        input.insert(0, -111)
        i += 1
    def cal(cur):
        if input[cur] != -111:return
        cal(2*cur+1)
        cal(2*cur+2)
        x = min(input[2*cur+2], input[2*cur+1])
        input[cur] = x
        input[2*cur+1] -= x
        input[2*cur+2] -= x
    cal(0)
    print(sum(input))
elif((n+1)//2 < len(input)):
    print("Incorrect Input")