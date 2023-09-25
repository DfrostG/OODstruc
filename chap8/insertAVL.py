class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
    def findHeight(root):
        if root is None:
            return 0
        left_height = Node.findHeight(root.left)
        right_height = Node.findHeight(root.right)
        return max(left_height, right_height) + 1
    
    def getBalance(self):
        return Node.findHeight(self.left) - Node.findHeight(self.right)

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, root: Node, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        
        balance = root.getBalance()
        if balance == 2:
            if root.left.getBalance() == -1:
                root.left = self.leftRotate(root.left)
            root = self.rightRotate(root)
        elif balance == -2:
            if root.right.getBalance() == 1:
                root.right = self.rightRotate(root.right)
            root = self.leftRotate(root)

        return root
    
    def leftRotate(self, root):
        y = root.right
        root.right = y.left
        y.left = root
        return y

    def rightRotate(self, root):
        y = root.left
        root.left = y.right
        y.right = root
        return y

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


A = AVL()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = A.insert(i)
    print(f"Insert : ( {i} )")
    A.printTree(root)
    print("--------------------------------------------------")