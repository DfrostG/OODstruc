class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def size(self):
        return len(self.items)
    
def parkingLot(max, parking_cars, state, target_car):
    max = int(max)
    if parking_cars == "0":
        cars = Stack()
        
    else:
        parking_cars = [int(car) for car in parking_cars.split(",")]
        cars = Stack()
        for car in parking_cars:
            cars.items.append(car)

    target_car = int(target_car)
    if state == "arrive":
        if target_car in cars.items:
            print(f"car {target_car} already in soi")
            print(cars.items)
            
        elif len(cars.items) == max:
            print(f"car {target_car} cannot arrive : Soi Full")
            print(cars.items)

        else:
            cars.items.append(target_car)
            print(f"car {target_car} arrive! : Add Car {target_car}")
            print(cars.items)

    elif state == "depart":
        if target_car not in cars.items and len(cars.items) == 0:
            print(f"car {target_car} cannot depart : Soi Empty")
            print(cars.items)
        
        elif target_car not in cars.items:
            print(f"car {target_car} cannot depart : Dont Have Car {target_car}")
            print(cars.items)

        else:
            temp_cars = Stack()
            for car in range(len(cars.items)-1, -1, -1):
                if cars.items[car] != target_car:
                    temp_cars.push(cars.pop())
                else:
                    cars.pop()
                    break
            
            for car in range(len(temp_cars.items)-1, -1, -1):
                cars.push(temp_cars.items[car])
            
            print(f"car {target_car} depart ! : Car {target_car} was remove")
            print(cars.items)

print("******** Parking Lot ********")
input_detail = input("Enter max of car,car in soi,operation : ").split()
parkingLot(*input_detail)