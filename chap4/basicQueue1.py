class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

inputstr = input("Enter Input : ").split(",")
queue = Queue()

for cmd in inputstr:
    if cmd[0] == "E":
        queue.enqueue(cmd.split()[1])
        print(queue.size())

    elif cmd[0] == "D":
        if queue.isEmpty() == False:
            print(f"{queue.dequeue()} 0")
        elif queue.isEmpty():
            print("-1")

if queue.isEmpty() == False:
    print(*queue.items)
elif queue.isEmpty():
    print("Empty")