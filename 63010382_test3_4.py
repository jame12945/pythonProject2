class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.item = item

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, item):
        past = Node(item)
        if self.root is None:
            self.root = past
        else:
            now = self.root
            x=1
            while(x==1):
                if item < now.item:
                    if now.left is None:
                        now.left = past
                        break
                    now = now.left
                else:
                    if now.right is None:
                        now.right = past
                        break
                    now = now.right
        return self.root


def height(objectt):
    if objectt == None: return "-1"
    leftheight = int(height(objectt.left)) + 1
    rightheight = int(height(objectt.right)) + 1
    return max(leftheight, rightheight)

print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
input = list(map(int, input("Enter Input : ").split()))
for i in input:
    tree.create(i)
print("Height = ", height(tree.root), end="\n\n")