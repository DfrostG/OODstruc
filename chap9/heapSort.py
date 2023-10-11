def insertMinHeap(h, i):
    insertEle = h[i]
    fi = (i - 1)//2
    while i > 0 and insertEle < h[fi]:
        h[i] = h[fi]
        i = fi
        fi = (i - 1)//2
    h[i] = insertEle

def delMin(h, last):
    insertEle = h[last]
    h[last] = h[0]
    hole = 0
    ls = hole*2+1
    found = False
    while ls < last and not found:
        if ls + 1 >= last:
            rs = ls
        else:
            rs = ls + 1
        if h[ls] < h[rs]:
            min = ls
        else:
            min = rs
        if h[min] < insertEle:
            h[hole] = h[min]
            hole = min
            ls = hole*2 + 1
        else:
            found = True
    h[hole] = insertEle
    

h = []
a = input("Enter list of number: ").split(",")
for i in range(len(a)):
    h.append(int(a[i]))
    insertMinHeap(h, i)
    

print("Heap: ", end="")
print(*h)
print("==== heap sort ====")
for last in range(len(h)-1, 0, -1):
    print(f"deleteMin = {h[0]} FindPlaceFor {h[last]}")
    delMin(h, last)
    print(*h)
    
print("==== Sorting a ====")
h.reverse()
print(*h)