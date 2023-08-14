class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        s = ""
        cur = self.head
        while cur != None:
            s += str(cur.value)
            cur = cur.next
        return s
    
    def forward(self, start, stop):
        self.forwardsize = 0
        cur = self.head
        while cur.value != start:
            cur = cur.next
        s = ""
        while cur.value != stop:
            s += str(cur.value) + "->"
            self.forwardsize += 1
            cur = cur.next
            if cur == None:
                cur = self.head
        s += str(cur.value)
        return s
    
    def backward(self, start, stop):
        self.backwardsize = 0
        cur = self.head
        while cur.value != start:
            cur = cur.next
        s = ""
        while cur.value != stop:
            s += str(cur.value) + "->"
            self.backwardsize += 1
            cur = cur.prev
            if cur == None:
                cur = self.tail
        s += str(cur.value)
        return s
            
print("***Railway on route***")
inp = input("Input Station name/Source, Destination, Direction(optional): ").split("/")
station = inp[0].split(",")
start, stop = inp[1].split(",")[0], inp[1].split(",")[1]

route = LinkedList()
for i in station:
    route.append(i)

if len(inp[1].split(",")) < 3:
    direction = None
else:
    direction = inp[1].split(",")[2]

if direction == "F":
    print(f"Forward Route: {route.forward(start, stop)},{route.forwardsize}")

elif direction == "B":
    print(f"Backward Route: {route.backward(start, stop)},{route.backwardsize}")

else:
    forwardstring = route.forward(start, stop)
    backwardstring = route.backward(start, stop)
    if route.forwardsize < route.backwardsize:
        print(f"Forward Route: {forwardstring},{route.forwardsize}")
    elif route.backwardsize < route.forwardsize:
        print(f"Backward Route: {backwardstring},{route.backwardsize}")
    elif route.forwardsize == route.backwardsize:
        print(f"Forward Route: {forwardstring},{route.forwardsize}")
        print(f"Backward Route: {backwardstring},{route.backwardsize}")