def insertionSort(arr):
    for i in range(1, len(arr)):
        iEle = arr[i]
        for j in range(i, -1, -1):
            if iEle < arr[j-1] and j > 0:
                arr[j] = arr[j - 1]
            else:
                arr[j] = iEle
                break
        print(f"Round {i} {arr}")
 
 
inp = list(map(int, input("Enter list for number: ").split(",")))
print("Before sort:", inp)
insertionSort(inp)
print("After sort:", inp)