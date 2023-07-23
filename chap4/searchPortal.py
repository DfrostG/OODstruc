class Queue():
    def __init__(self):
        self.items = []

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)
    
    def peek(self):
        self.items[-1]

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
class Room():
    def __init__(self, width, height):
        self.queue = Queue()
        self.width = width
        self.height = height
        self.map = []
        self.maze = []
        self.start_pos = None

    def create_map(self, room_string):
        room_lines = room_string.split(",")

        if len(room_lines) != self.height:
            return "Invalid map input."
        
        for line in room_lines:
            if len(line) != self.width:
                return "Invalid map input."
            self.map.append(line)

    def find_start_pos(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] == "F":
                    self.start_pos = (j, i)
                    self.queue.enQueue(self.start_pos)
                    self.maze.append(self.start_pos)
                    break
            if self.start_pos != None:
                break
        if self.start_pos == None:
            return "Invalid map input."
        
    def find_portal(self):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        while not self.queue.isEmpty():
            print(f"Queue: {self.queue.items}")

            x, y = self.queue.deQueue()

            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy

                if 0 <= x2 < self.width and 0 <= y2 < self.height:
                    pos = self.map[y2][x2]
                    if pos == "O":
                        return "Found the exit portal."
                    elif pos == "_" and (x2, y2) not in self.maze:
                        self.maze.append((x2,y2))
                        self.queue.enQueue((x2, y2))

        return "Cannot reach the exit portal."
    
input_str = input("Enter width, height, and room: ")
width, height, room = input_str.split()
room_obj = Room(int(width), int(height))
temp = room_obj.create_map(room)
if temp != None:
    print(temp)
else:
    temp2 = room_obj.find_start_pos()
    if temp2 != None:
        print(temp2)
    else:
        print(room_obj.find_portal())