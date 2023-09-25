class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

customer = 0
vans, inp = input("Enter Input : ").split("/")

rent_days = []
for i in inp.split():
    rent_days.append(int(i))

vans_number = []
for i in range(int(vans)):
    vans_number.append(Node(0))

while rent_days:
    for i in range(len(vans_number)):
        if vans_number[i].data == 0 and rent_days:
            customer += 1
            day = rent_days.pop(0)
            vans_number[i].data = day
            print(f"Customer {customer} Booking Van {i+1} | {day} day(s)")
            vans_number[i].data -= 1
        elif vans_number[i].data > 0:
            vans_number[i].data -= 1