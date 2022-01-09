class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        if self.root is None:
            self.root = Node(data)
            return self.root
        temp = self.root
        while True:
            if temp.data < data:
                if temp.right is None:
                    temp.right = Node(data)
                    break
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = Node(data)
                    break
                else:
                    temp = temp.left
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def Breadth(self, root):
        if root is None:
            return

        queue = [ ]
        queue.append(root)

        while len(queue) > 0:
            print(queue [ 0 ].data, end=' ')
            node = queue.pop(0)

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def Huffman(self, inp):
        lis = [ ]
        nodeList = [ ]

        for i in range(len(inp)):
            if inp [ i ] in lis:
                pass
            else:
                lis.append(inp [ i ])
                count = inp.count(inp [ i ])
                node = Node(inp [ i ], count)
                nodeList.append(node)

        nodeList.sort(key=lambda x: x.data, reverse=False)
        nodeList.sort(key=lambda x: x.freq, reverse=False)
        if len(nodeList) >= 2:
            for i in range(len(nodeList) - 2, 0, -1):
                if nodeList [ i ].freq == nodeList [ i + 1 ].freq:
                    if nodeList [ i + 1 ].data == '*':
                        nodeList [ i ], nodeList [ i + 1 ] = nodeList [ i + 1 ], nodeList [ i ]

        while len(nodeList) >= 2:
            tempNode = Node('*', nodeList [ 0 ].freq + nodeList [ 1 ].freq)
            tempNode.left = nodeList.pop(0)
            tempNode.right = nodeList.pop(0)

            nodeList.append(tempNode)

            # nodeList.sort(key=lambda x: x.data, reverse=False)
            nodeList.sort(key=lambda x: x.freq, reverse=False)
            if len(nodeList) >= 2:
                for i in range(len(nodeList) - 2, -1, -1):
                    if nodeList [ i ].freq == nodeList [ i + 1 ].freq:
                        if nodeList [ i + 1 ].data == '*' and nodeList [ i ].data != '*':
                            nodeList [ i ], nodeList [ i + 1 ] = nodeList [ i + 1 ], nodeList [ i ]

        return nodeList.pop()

    def encode(self, node, dic={}, s=""):
        if node.right != None:
            self.encode(node.right, dic, s=s + "1")
            self.encode(node.left, dic, s=s + "0")
        else:
            dic [ node.data ] = s
            s = ""
        return dic


T = BST()
inp = input("Enter Input : ")
temp = T.Huffman(inp)

x = T.encode(temp)
print(x)

T.printTree(temp)

print("Encoded! : ", end='')
for i in inp:
    print(x [ i ], end='')

