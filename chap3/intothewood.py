class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    

inputstr = input("Enter Input : ").split(",")
stack = Stack()
for curtree in inputstr:
    act = curtree.split()[0]

    if act == "A":
        height = int(curtree.split()[1])
        while stack.isEmpty() == False and stack.peek() <= height:
            stack.pop()
        stack.push(height)
    
    if act == "B":
        print(stack.size())