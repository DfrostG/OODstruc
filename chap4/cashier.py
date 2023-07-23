class Queue:
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
    
main = Queue()
cashier1 = Queue()
cashier2 = Queue()
queue, time = input("Enter people and time : ").split(" ")

max_cashier1, max_cashier2 = 5, 5
for i in queue:
    main.enqueue(i)

count = 0
minute = int(time)
while count < minute:
    count += 1
    if count % 2 == 0:
        if not cashier2.isEmpty():
            cashier2.dequeue()

    if (count - 1) % 3 == 0:
        if not cashier1.isEmpty():
            cashier1.dequeue()

    if cashier1.size() < max_cashier1:
        if main.isEmpty() == False:
            cashier1.enqueue(main.dequeue())

    elif cashier2.size() < max_cashier2:
        if main.isEmpty() == False:
            cashier2.enqueue(main.dequeue())

    print(f"{count} {main.items} {cashier1.items} {cashier2.items}")