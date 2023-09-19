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
    
    def checkpos(self, num):
        if self.root.data == num:
            return "Root"
        return self.checkpos_(num, self.root)

    def checkpos_(self, num, root):
        if root is None:
            return "Not exist"
        elif root.data < num:
            return self.checkpos_(num, root.right)
        elif root.data > num:
            return self.checkpos_(num, root.left)
        elif num == root.data:
            if root.right is None and root.left is None:
                return "Leaf"
        return "Inner"        

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
print(T.checkpos(inp[0]))