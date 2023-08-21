def diff(sour:int, bitter:int):
    return abs(sour - bitter)

def find(length, sour, bitter):
    global best
    if length == length_inp:
        if bitter > 0 and diff(sour, bitter) < best:
            best = diff(sour, bitter)
    else:
        find(length + 1, sour * sour_list[length], bitter + bitter_list[length])
        find(length + 1, sour, bitter)

inp = input("Enter Input : ").split(",")

length_inp = len(inp)

sour_list = []
bitter_list = []
best = 9999

for i in inp:
    item = i.split(" ")
    sour_list.append(int(item[0]))
    bitter_list.append(int(item[1]))

find(0, 1, 0)

print(best)