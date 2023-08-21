def find_binary(n, prefix=""):
    if n == 0:
        print(prefix)
    else:
        find_binary(n - 1, prefix + "0")
        find_binary(n - 1, prefix + "1")

input_number = int(input("Enter Number : "))
if input_number < 0:
    print(f'Only Positive & Zero Number ! ! !')

elif input_number == 0:
    print("0")

else:
    find_binary(input_number)