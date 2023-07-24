class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop(0)

    def peek(self):
        self.items[-1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

queue = Queue()
message = input("Enter Input : ").split(",")

for cmd in message:

    if cmd[0] == "E":
        value = cmd[2:]
        queue.enqueue(value)
        top_value = queue.peek()
        if top_value != -1:
            print(f"Add {value} index is {queue.size() - 1}")
    
    elif cmd == "D":
        if queue.isEmpty():
            print("-1")
        else:
            val = queue.dequeue()
            print(f"Pop {val} size in queue is {queue.size()}")

if queue.isEmpty():
    print("Empty")
else:
    print("Number in Queue is : ", queue.items)