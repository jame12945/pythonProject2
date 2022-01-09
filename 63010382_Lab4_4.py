class Queue:
    def __init__(self, que):
        self.item = []  # for id
        self.num = []   # for depart num
        self.bool = que   # dict()

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        return 'Number in Queue is :  ' + str(self.item)

    def deQ(self):
        if self.isEmpty():
            return 'Empty'
        self.num.pop(0)
        return self.item.pop(0)

    def enQ(self, i):
        myValue = 0
        for key, value in self.bool.items():
            if key == i:
                myValue = value

        if self.isEmpty():
            self.item.append(i)
            self.num.append(myValue)
        else:
            have = False
            for j in range(self.size() - 1, -1, -1):
                if self.num[j] == myValue:
                    self.item.insert(j + 1, i)
                    self.num.insert(j + 1, myValue)
                    have = True
                    break
            if have is False:
                self.item.append(i)
                self.num.append(myValue)

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)


list,num1= input('Enter Input : ').split('/')
bool = dict()
for i in list.split(','):
    i = i.split()
    bool[int(i[1])] = int(i[0])

mainQ = Queue(bool)

for i in num1.split(','):
    i = i.split()
    if i[0] == 'E':
        mainQ.enQ(int(i[1]))
    elif i[0] == 'D':
        print(mainQ.deQ())