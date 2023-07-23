def num_grid(lst):

    row = len(lst)
    col = len(lst[0])
    
    lst = [['0' if cell == '-' else cell for cell in row] for row in lst]

    for i in range(row):
        for j in range(col):

            if lst[i][j] == '#': 
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < row and 0 <= y < col and lst[x][y] != '#':
                        lst[x][y] = str(int(lst[x][y]) + 1)
    return lst

print("*** Minesweeper ***")
lst_input = []
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")