lst, start = input("Enter a list of points: ").split("/")
lst = lst.split(",")

if start not in lst:
    start = start.split()
    start[0], start[1] = float(start[0]), float(start[1])
    for i in range(len(lst)):
        temp = lst[i].split()
        lst[i] = [float(temp[0]), float(temp[1])]
    print(f"{start} is not in {lst}")
    quit()
 
lst = lst[lst.index(start):] + lst[:lst.index(start)]
ans = []
for i in range(len(lst)):
    temp = lst[i].split()
    lst[i] = [float(temp[0]), float(temp[1])]

ans.append(list(lst.pop(0)))

def arrange(lst : list, ans: list):
    min = 99999
    index = 0
    while len(lst) > 0: 
        for i in range(len(lst)):
            temp = (abs(ans[-1][0] - lst[i][0])**2 + abs(ans[-1][1] - lst[i][1])**2)**0.5
            if temp < min:
                min = temp
                index = i
        min = 99999
        ans.append(lst.pop(lst.index(lst[index])))

arrange(lst, ans)

for i in range(len(ans) - 1):
    result = format((abs(ans[i + 1][0] - ans[i][0])**2 + abs(ans[i + 1][1] - ans[i][1])**2)**0.5, ".4f")
    print(f"{ans[i]} -> {ans[i + 1]} | The distance is {format(result)}")