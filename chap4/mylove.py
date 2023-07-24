class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

act = ["Eat", "Game", "Learn", "Movie"]
place = ["Res.", "ClassR.", "SuperM.", "Home"]

me, you, point = Queue(), Queue(), 0
list_me, list_you = [], []

inputstr = input("Enter Input : ").split(",")

for val in inputstr:
    ac = val.split(" ")
    me.enqueue(ac[0])
    you.enqueue(ac[1])

# print(f"My Queue = {me.items}")
# print(f"Your Queue = {you.items}")
print("My Queue =", *me.items)
print("Your Queue =", *you.items)


while not me.isEmpty():
    top_me, top_you = me.dequeue(), you.dequeue()

    list_me.append(f"{act[int(top_me[0])]}:{place[int(top_me[2])]}")
    list_you.append(f"{act[int(top_you[0])]}:{place[int(top_you[2])]}")

    if top_me[0] == top_you[0] and top_me[2] != top_you[2]:
        point += 1

    elif top_me[2] == top_you[2] and top_me[0] != top_you[0]:
        point += 2
    
    elif top_me[0] == top_you[0] and top_me[2] == top_you[2]:
        point += 4

    elif top_me[0] != top_you[0] and top_me[2] != top_you[2]:
        point -= 5

print("My   Activity:Location = ", end = "")
print(", ".join(list_me))
print("Your Activity:Location = ", end = "")
print(", ".join(list_you))

if point >= 7:
    print(f"Yes! You're my love! : Score is {point}.")

elif 0 < point and point < 7:
    print(f"Umm.. It's complicated relationship! : Score is {point}.")

elif point <= 0:
    print(f"No! We're just friends. : Score is {point}.")
