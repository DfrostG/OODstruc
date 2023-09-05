class Node:
    def __init__(self, data, next: 'Node' = None):
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

    def pop(self, pos):
        if self.isEmpty() or pos < 0 or pos >= self.size():
            return "Out of Range"
        
        if pos == 0:
            removed_value = self.head.data
            self.head = self.head.next
        else:
            prev = None
            cur = self.head
            count = 0
            while cur != None and count < pos:
                prev = cur
                cur = cur.next
                count += 1
            removed_value = cur.data
            prev.next = cur.next
        return removed_value
    
    def isEmpty(self):
        return self.head == None
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur is not None:
            s += str(cur.data) + " "
            cur = cur.next
        return s
    
    def search(self, item):
        cur = self.head
        index = 0
        while cur is not None:
            if cur.data == item:
                return "Found"
            cur = cur.next
            index += 1
        return "Not Found"
    
    def size(self):
        size = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            size += 1
        return size


l = LinkedList()
l.append(4)
l.append(2)
l.append(1)
print(l)
print(l.pop(0))
