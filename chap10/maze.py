def find_min_index(arr):
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def find_max_index_in_row(min_idx, row, col):
    max_idx = 0
    for i in range(col):
        idx = row * min_idx + i
        if idx < len(arr) and arr[idx] > arr[max_idx]:
            max_idx = idx
    return max_idx

def find_max_index_in_col(max_idx, row):
    max_index = 0
    for i in range(row):
        idx = row * i + max_idx
        if idx < len(arr) and arr[idx] > arr[max_index]:
            max_index = idx
    return max_index


table, inp = input("input : ").split(",")
table = list(map(int, table.split()))
arr = list(map(int, inp.split()))
row, col = table[0], table[1]

min_idx = find_min_index(arr) // col
row_max_idx = find_max_index_in_row(min_idx, row, col)
col_max_idx = find_max_index_in_col(row_max_idx % row, row)
print(f"{arr[col_max_idx]}")