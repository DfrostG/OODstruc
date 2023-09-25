def nameValue(val):
    sum = 0
    for i in [*val]:
        sum += ord(i)
    return sum


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self) -> str:
        return str(self.data) + nameValue(self.data)

    


class AVL_Tree(object):
    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif nameValue(data) < nameValue(root.data):
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1

        balance = self.getBalance(root)
        if balance > 1:
            if nameValue(data) < nameValue(root.left.data):
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if nameValue(data) > nameValue(root.right.data):
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete(self, root: Node, data):
        if root is None:
            return root
        elif nameValue(data) < nameValue(root.data):
            root.left = self.delete(root.left, data)
        elif nameValue(data) > nameValue(root.data):
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        
        if root is None:
            return root
        
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def leftRotate(self, root):
        y = root.right
        T2 = y.left
        y.left = root
        root.right = T2
        root.height = max(self.getHeight(root.left),self.getHeight(root.right)) + 1
        y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1
        return y

    def rightRotate(self, root):
        y = root.left
        T3 = y.right
        y.right = root
        root.left = T3
        root.height = max(self.getHeight(root.left),self.getHeight(root.right)) + 1
        y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1
        return y
    
    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def printTree(self, root: Node, level=0):
        if root != None:
            indent = "    " * level
            print(indent + root.data,"(" + str(nameValue(root.data)) + ")")
            self.printTree(root.left, level + 1)
            if (root.left is None and root.right is not None) or \
            (root.left is not None and root.right is None):
                print(indent + "    " + "*")
            self.printTree(root.right, level + 1)

avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(root, data)
    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")