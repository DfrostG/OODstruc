class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return -1
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return -1
    
    def size(self):
        return len(self.items)
    
stack = Stack()    
messages = input("Enter Input : ").split(",")

for cmd in messages:

    if cmd[0] == "A":
        value = int(cmd[2:])
        stack.push(value)
        print("Add =", value, "and Size =", stack.size())
    
    elif cmd == "P":
        top_value = stack.peek()
        if top_value != -1:
            print("Pop =", top_value, "and Index =", stack.size() - 1)
            stack.pop()
        
        else:
            print("-1")

if stack.size() > 0:
    print("Value in Stack =", *stack.items)
    
else:
    print("Value in Stack = Empty")