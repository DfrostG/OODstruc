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

    def findMinRoot(self, root):
        if root.left is None:
            return root.data
        return self.findMinRoot(root.left)
    
    def findNode(self, data):
        self.root = self.findNode_(self.root, data)

    def findNode_(self, root, data):
        if root is None:
            return None
        if root.data == data:
            return root
        if data < root.data:
            root.left = self.findNode_(root.left, data)
        else:
            root.right = self.findNode_(root.right, data)
        return self.findNode_(self.root, data)

    def deleteNode(self, data):
        self.root, c =self.deleteNode_(self.root, data)
        return c
    
    def deleteNode_(self, root : Node, key : int):
        checker = False
        if root is None:
            return root, False
        if int(key) < int(root.data):
            root.left, checker = self.deleteNode_(root.left, key)
        elif int(key) > int(root.data):
            root.right, checker = self.deleteNode_(root.right, key)
        else:
            checker = True
            if root.left is None or root.right is None:
                if root.right is None:
                    root = root.left
                else:
                    root = root.right
            else:
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.data = temp.data
                root.right, checker = self.deleteNode_(root.right, temp.data)
        return root, checker
    

T = BST()
inp = input('Enter Input : ').split(",")
for cmd in inp:
    cmd = cmd.split()
    if cmd[0] == "i":
        print(f"insert {cmd[1]}")
        T.insert(int(cmd[1]))
        T.printTree(T.root)
    elif cmd[0] == "d":
        print(f"delete {cmd[1]}")
        c = T.deleteNode(int(cmd[1]))
        if not c:
            print("Error! Not Found DATA")
        T.printTree(T.root)