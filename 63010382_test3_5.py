class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
class Binary:
    def __init__(self):
        self.root = None

    def insert(self, data, root):
        if root == None:
            return Node(data)
        else:
            if (root.data == data):
                return root
            if (root.data > data):
                root.left = self.insert(data,root.left)
            else:
                root.right = self.insert(data,root.right)
        return root

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def findMax(self, root):
        if root is None:
            return float('-inf')

        respiratory = root.data
        leftres = self.findMax(root.left)
        rightres = self.findMax(root.right)

        if leftres > respiratory:
            respiratory = leftres
        if rightres > respiratory:
            respiratory = rightres
        return respiratory

    def findMin(self, root):
        if root == None:
            return float('inf')
        respiratory= root.data
        rightres= self.findMin(root.right)
        leftres = self.findMin(root.left)
        if rightres < respiratory:
            respiratory = rightres
        if leftres < respiratory:
            respiratory = leftres
        return respiratory


Tree = Binary()
input = [ int(i) for i in input('Enter Input : ').split() ]
root = Node(input.pop(0))
for i in input:
    root = Tree.insert(i, root)
Tree.printTree(root)
print('--------------------------------------------------')
print("Min :", Tree.findMin(root))
print("Max :", Tree.findMax(root))