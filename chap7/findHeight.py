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
        self.level = 0

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
        self.level += 1
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def findHigh(self):
        def find(root, level):
            if root == None:
                return level
            else:
                return max(find(root.left, level+1), find(root.right, level+1))
        return find(self.root, 0)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
# T.printTree(root)
print(f"Height of this tree is : {T.findHigh() - 1}")