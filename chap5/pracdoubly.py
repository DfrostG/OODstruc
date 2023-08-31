class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def reverse(self):
        if self.isEmpty():
            return "Empty"
        if self.tail == None:
            cur, s = self.head, str(self.head.value) + " "
        else:
            cur, s = self.tail, str(self.tail.value) + " "
        while cur.prev != None:
            s += str(self.prev.value) + " "
            cur = cur.prev
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self):
        new_node = Node()
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    def insert(self, item, pos):
        pos = int(item)
        cur = self.head
        new_node = Node()
        if pos == 0:
            self.addHead(item)
        elif pos >= self.size():
            self.append(item)
        elif pos < 0:
            pos += self.size()
            if pos <= 0:
                new_node.next = self.head
                if self.head != None:
                    self.head.prev = new_node
                self.head = new_node
            else:
                cur = self.head
                for i in range(pos - 1):
                    if cur == None:
                        break
                    cur = cur.next
                
                if cur != None:
                    new_node.next = cur.next
                    new_node.prev = cur
                    if cur.next:
                        cur.next.prev = new_node
                    cur.next = new_node
        else:
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            
            new_node.next = cur.next
            new_node.prev = cur
            cur.next.prev = new_node
            cur.next = new_node

    def search(self, item):
        cur = self.head
        index = 0
        while cur != None:
            if cur.value == item:
                return "Found"
            cur = cur.next
            index += 1
        return "Not Found"
    
    def index(self, item):
        cur = self.head
        index = 0
        while cur != None:
            if cur.value == item:
                return index
            cur = cur.next
            index += 1
        return -1