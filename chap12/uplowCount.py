print(" *** String count ***")
message = input("Enter message : ")

def count_letters(str):
    lowercase_count = 0
    uppercase_count = 0
    unique_lowercase_letters = set()
    unique_uppercase_letters = set()

    for char in str:
        if char.islower():
            lowercase_count += 1
            unique_lowercase_letters.add(char)
        elif char.isupper():
            uppercase_count += 1
            unique_uppercase_letters.add(char)

    sorted_uppercase_letters = sorted(unique_uppercase_letters)
    sorted_lowercase_letters = sorted(unique_lowercase_letters)
    
    return uppercase_count, lowercase_count, sorted_uppercase_letters, sorted_lowercase_letters

uppercase, lowercase, sorted_uppercase_letters, sorted_lowercase_letters = count_letters(message)


print("No. of Upper case characters :", uppercase)
print("Unique Upper case characters :", '  '.join(sorted_uppercase_letters))
print("No. of Lower case Characters :", lowercase)
print("Unique Lower case characters :", '  '.join(sorted_lowercase_letters))

