print(" *** Summation of each digit ***")
num = int(input("Enter a positive number : "))


def getSum(num):

    sum =0 

    for digit in str(num):
        sum += int(digit)
    return sum

print("Summation of each digit = ", getSum(num))
