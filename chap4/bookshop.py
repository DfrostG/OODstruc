class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def size(self):
        return len(self.items)
    
book_shelf = Queue()
book_in_shelf, commands = input("Enter Input : ").split("/")

book = book_in_shelf.split(" ")
cmd = commands.split(",")

for item in book:
    book_shelf.enqueue(item)

for item in cmd:
    ed = item[0]
    id_book = item[2:]

    if ed == "D":
        book_shelf.dequeue()

    elif ed == "E":
        book_shelf.enqueue(id_book)

if len(book_shelf.items) != len(set(book_shelf.items)):
    print("Duplicate")
else:
    print("NO Duplicate")