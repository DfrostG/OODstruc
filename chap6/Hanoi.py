def move(n, A, B, C, maxn):
    if n == 1:
        C[0].append(A[0].pop())
        print(f"move {n} from  {A[1]} to {C[1]}")
        printHanoi(maxn)
        return
    move(n - 1, A, C, B, maxn)
    C[0].append(A[0].pop())
    print(f"move {n} from  {A[1]} to {C[1]}")
    printHanoi(maxn)
    move(n - 1, B, A, C, maxn)

def printHanoi(n):
    global a, b, c
    if n < 0:
        return
    
    if len(a[0]) <= n:
        print("|  ", end = "")
    else:
        print(f"{a[0][n]}  ", end = "")

    if len(b[0]) <= n:
        print("|  ", end = "")
    else:
        print(f"{b[0][n]}  ", end = "")

    if len(c[0]) <= n:
        print("|")
    else:
        print(f"{c[0][n]}")
    return printHanoi(n - 1)

def add_number(n):
    if n == 1:
        global a
        a[0].append(str(n))
        return
    a[0].append(str(n))
    add_number(n - 1)

n = int(input("Enter Input : "))
a = [[], "A"]
b = [[],"B"]
c = [[],"C"]
add_number(n)
printHanoi(n)
move(n, a, b, c, n)