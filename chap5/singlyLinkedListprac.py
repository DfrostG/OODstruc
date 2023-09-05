class Node:
    def __init__(self, data, next: "Node" = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def addHead(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        cur = Node(data)
        cur.next = self.head
        self.head = cur

    def pop(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            temp = self.head
            self.head = None
            return temp.data

        cur = self.head
        while cur.next is not None and cur.next.next is not None:
            cur = cur.next
        
        temp = cur.next
        cur.next = None
        return temp.data
    
    def size(self):
        size = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            size += 1
        return size
    
    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, ""
        while cur is not None:
            s += str(cur.data) + " "
            cur = cur.next
        return s

    
l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
print(l)
print(f"Size is {l.size()}")
print(l.pop())
print(l.pop())
print(l.pop())
print(f"Size is {l.size()}")
