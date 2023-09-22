class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)
    
    def setHeight(self, root):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a, b)
        return self.height
    
    def getHeight(self, node):
        if node is None:
            return -1
        return node.height
    
    def balanceValue(self, root = None):
        if root is None:
            self.root = None
        return root

class AVL:
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


A = AVL()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = A.insert(i)
A.printTree(root)