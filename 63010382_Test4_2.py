class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)


class AVLTREE:
    def insert(self, root, data):
        if not root:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        if data >= root.data:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getheight(root.left),
                              self.getheight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and data >= root.left.data:
            root.left = self.left(root.left)
            return self.right_R(root)

        elif balance < -1 and data < root.right.data:
            root.right = self.right_R(root.right)
            return self.left_R(root)
        elif balance > 1 and data < root.left.data:
            return self.right_R(root)

        if balance < -1 and data >= root.right.data:
            return self.left_R(root)

        return root

    def getheight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getheight(root.left) - self.getheight(root.right)

    def left_R(self, z):

        y = z.right

        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getheight(z.left),
                           self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),
                           self.getheight(y.right))
        return y

    def right_R(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getheight(z.left),
                           self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),
                           self.getheight(y.right))

        return y

    def preoder(self, root):
        if root is not None:
            print(root.data, "", end='')
            self.preoder(root.left)
            self.preoder(root.right)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, "", end='')
            self.inorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, "", end='')


T = AVLTREE()
root = None
print(" *** AVL Tree ***")
inp = [ int(i) for i in input('Enter some numbers : ').split() ]
for i in inp:
    root = T.insert(root, i)

print("in_order  --> ", end='')
T.inorder(root)
print()
print("preorder  --> ", end='')
T.preoder(root)
print()
print("postorder --> ", end='')
T.postorder(root)
print()