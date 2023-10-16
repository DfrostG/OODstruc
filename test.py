size = int(input("Enter size : "))
# for i in range(inp):
#     print("*", end="")
# print("*")
# print("_" * (int(inp) - 2))
# print("*")

# size = 5  # You can change this to the desired size

for i in range(size):
    # Loop through columns
    for j in range(size):
        # Check if it's an edge or the center
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    # Move to the next line after each row
    print()