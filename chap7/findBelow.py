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
        
    def findBelow(self, data, r):
        if r:
            self.findBelow(data, r.left)
            if int(data) > int(r.data):
                print(r.data, end=" ")
            self.findBelow(data, r.right)

T = BST()
inp =  input('Enter Input : ').split("|")
temp = [int(i) for i in inp[0].split()]
for i in temp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(f"Below {inp[1]} : ", end="")
if T.findBelow(inp[1],root) == "" :
    T.findBelow(inp[1],root)
else:
    print("Not have")