class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.snext = None

class SNode():
    def __init__(self, value):
        self.value = value
        self.next = None

class link:
    def __init__(self):
        self.head = None

    def next_node(self, new_node):
        if self.search(new_node.value) != None:
            return None
        elif self.search(new_node.value) == None:
            if self.head == None:
                self.head = new_node
            else:
                cur_node = self.head
                while cur_node.next != None:
                    cur_node = cur_node.next
                cur_node.next = new_node

    def search(self, value):
        cur_node = self.head
        while cur_node != None:
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.next
        return None
    
    def next_secondary_node(self, n, s_new_node):
        temp = self.search(n)
        if temp.snext == None:
            temp.snext = s_new_node
        else:
            s_cur = temp.snext
            while s_cur.next != None:
                s_cur = s_cur.next
            s_cur.next = s_new_node

    def show_all(self):
        cur = self.head
        while cur != None:
            print(f"{cur.value} : ", end = "")
            s_cur = cur.snext
            while s_cur != None:
                print(f"{s_cur.value}", end = ",")
                s_cur = s_cur.next
            cur = cur.next    
            print()

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(Node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],SNode(h[1]))
l.show_all()