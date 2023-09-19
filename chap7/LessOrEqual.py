class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def insert_ (root, data):
            if root is None:
                return Node(data)
            else:
                if data < root.data:
                    root.left = insert_(root.left, data)
                else:
                    root.right = insert_(root.right, data)
            return root
        self.root = insert_(self.root, data)
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def findless(self, data):
        return self.findless_(self.root, data)

    def findless_(self, root, data):
        if root is None:
            return 0
        size = 0
        size += self.findless_(root.left, data)
        if data >= root.data:
            size += 1
        size += self.findless_(root.right, data)
        return size


T = BST()
num, data = input("Enter Input : ").split("/")
inp = [int(i) for i in num.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(T.findless(int(data)))