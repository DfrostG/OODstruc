class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
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
            cur , s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            self.tail = new_node
            new_node.previous = cur

    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            p.next = self.head
            self.head.previous = p
            self.head = p
        
    def insert(self, pos, item):
        new_node = Node(item)
        if pos == 0:
            self.addHead(item)
        elif pos >= self.size():
            self.append(item)
        elif pos < 0:
            pos = self.size() + pos
            if pos <= 0:
                new_node.next = self.head
                if self.head != None:
                    self.head.previous = new_node
                self.head = new_node
            else:
                cur = self.head
                for i in range(pos - 1):
                    if cur == None:
                        break
                    cur = cur.next
                
                if cur != None:
                    new_node.next = cur.next
                    new_node.previous = cur
                    if cur.next:
                        cur.next.previous = new_node
                    cur.next = new_node
        else:
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
                
            new_node.next = cur.next
            new_node.previous = cur
            cur.next.previous = new_node
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
    
    def size(self):
        count = 0
        cur = self.head
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def pop(self, pos):
        if pos < 0 or pos >= self.size():
            return "Out of Range"
        if pos == 0:
            return self.removeHead()
        elif pos == self.size() - 1:
            return self.removeTail()
        else:
            cur = self.head
            for i in range(pos):
                cur = cur.next
            cur.previous.next = cur.next
            cur.next.previous = cur.previous
            return "Success"

    def removeHead(self):
        if self.isEmpty():
            return "Empty"
        data = self.head.value
        if self.head.next == None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        return "Success"

    def removeTail(self):
        if self.isEmpty():
            return "Empty"
        data = self.tail.value
        if self.tail.previous == None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        return "Success"
    
L = LinkedList()
inp = input("Enter Input : ").split(",")
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())