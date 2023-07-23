class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Client:
    def __init__(self, arrive, coffee_time, id):
        self.arrive = arrive
        self.coffee_time = coffee_time
        self.client_id = id

class Barista:
    def __init__(self):
        self.status = True
        self.client_id = None
        self.make_coffee_time = None

class Cafe:
    def __init__(self):
        self.clients = Queue()
        self.cafe_queue = Queue()
        self.barista_1 = Barista()
        self.barista_2 = Barista()
        
    def open(self, clients):
        time = 0
        longest_wait = 0
        longest_wait_client_id = None
        self.add_clients(clients)

        while not self.cafe_queue.isEmpty() or not self.clients.isEmpty() or (not self.barista_1.status or not self.barista_2.status):
            while not self.clients.isEmpty() and self.clients.items[0].arrive == time:
                self.cafe_queue.enqueue(self.clients.dequeue())
            
            if not self.barista_1.status or not self.barista_2.status: 
                if (self.barista_1.make_coffee_time == 0 and self.barista_2.make_coffee_time == 0) and (not self.barista_1.status and not self.barista_2.status):
                    self.barista_1.status = True
                    self.barista_2.status = True
                    self.barista_1.make_coffee_time = -1
                    self.barista_2.make_coffee_time = -1
                    if self.barista_2.client_id > self.barista_1.client_id:
                        print(f"Time {time} customer {self.barista_1.client_id} get coffee")
                        print(f"Time {time} customer {self.barista_2.client_id} get coffee")
                    else:
                        print(f"Time {time} customer {self.barista_2.client_id} get coffee")
                        print(f"Time {time} customer {self.barista_1.client_id} get coffee")
                if not self.barista_1.status:
                    if self.barista_1.make_coffee_time == 0:
                        self.barista_1.status = True
                        print(f"Time {time} customer {self.barista_1.client_id} get coffee")
                    elif self.barista_1.make_coffee_time > 0:
                        self.barista_1.make_coffee_time -= 1
                if not self.barista_2.status:
                    if self.barista_2.make_coffee_time == 0:
                        self.barista_2.status = True
                        print(f"Time {time} customer {self.barista_2.client_id} get coffee")
                    elif self.barista_2.make_coffee_time > 0:
                        self.barista_2.make_coffee_time -= 1
                    
            if self.barista_1.status and not self.cafe_queue.isEmpty():
                temp = self.cafe_queue.dequeue()
                self.barista_1.status = False
                self.barista_1.client_id = temp.client_id
                self.barista_1.make_coffee_time = temp.coffee_time-1
                if time - temp.arrive > longest_wait:
                    longest_wait = time - temp.arrive
                    longest_wait_client_id = temp.client_id
            if self.barista_2.status and not self.cafe_queue.isEmpty():
                temp = self.cafe_queue.dequeue()
                self.barista_2.status = False
                self.barista_2.client_id = temp.client_id
                self.barista_2.make_coffee_time = temp.coffee_time-1
                if time - temp.arrive > longest_wait:
                    longest_wait = time - temp.arrive
                    longest_wait_client_id = temp.client_id
                    
            time += 1
        if longest_wait_client_id == None:
            print("No waiting")
        else:
            print(f"The customer who waited the longest is : {longest_wait_client_id}")
            print(f"The customer waited for {longest_wait} minutes")
        
        
    def add_clients(self, clients):
        sorted_clients = sorted(clients, key=lambda x: x[0])
        client_id = 1
        for client in sorted_clients:
            self.clients.enqueue(Client(client[0], client[1], client_id))
            client_id += 1
            
    
    
print(" ***Cafe***")
inputs = input("Log : ")
clients = [[int(x) for x in inp.split(",")] for inp in inputs.split("/")]
cafe = Cafe()
cafe.open(clients)