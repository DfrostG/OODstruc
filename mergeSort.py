def mergeSort(arr):    #7 3 2 16 24 4 11 9
    if len(arr) <= 1:
        return arr
    m = len(arr)//2
    left_sorted = mergeSort(arr[0:m]) #2 3 7 16
    right_sorted = mergeSort(arr[m:]) #4 9 11 24
    result = []
    while left_sorted and right_sorted:
        if right_sorted[0] < left_sorted[0]:  
            result.append(right_sorted.pop(0))
        else:
            result.append(left_sorted.pop(0))
    while left_sorted:
        result.append(left_sorted.pop(0))
    while right_sorted:
        result.append(right_sorted.pop(0)) 
    return result

# inp = list(map(int, input("Enter Input : ").split()))
# print(mergeSort(inp))

inp = [int(x) for x in input("Enter input : ").split()]
print(mergeSort(inp))