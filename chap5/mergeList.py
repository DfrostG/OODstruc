class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = p

    def isEmpty(self):
        return self.head == None
    
    def display(self):
        p = self.head
        while p != None:
            print(p.value + " ", end = '')
            p = p.next
        print()

val1, val2 = input("Enter Input (L1,L2) : ").split(" ")
l1 = val1.split("->")
l2 = val2.split("->")

linkedlist1 = LinkedList()
linkedlist2 = LinkedList()
mergelist = LinkedList()

for i in l1:
    linkedlist1.append(i)

for i in l2:
    linkedlist2.append(i)

for i in l1:
    mergelist.append(i)

for i in reversed(l2):
    mergelist.append(i)

print("L1    : ", end = "")
linkedlist1.display()

print("L2    : ", end = "")
linkedlist2.display()

print("Merge : ", end = "")
mergelist.display()