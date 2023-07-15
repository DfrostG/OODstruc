print(" *** Divisible number ***")
num = int(input("Enter a positive number : "))
factors = []
count = 0

if num > 0:
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            count += 1
    print("Output ==>", *factors, "\nTotal ==>", count)
elif num == 0:
    print("0 is OUT of range !!!")