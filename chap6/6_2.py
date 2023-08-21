def palindrome(inp:str):
    if len(inp) <= 1:
        return True
    else:
        if inp[0] == inp[-1]:
            return palindrome(inp[1:-1])
        else:
            return False
    
inp = input("Enter Input : ")
if palindrome(inp):
    print(f"'{inp}' is palindrome")
else:
    print(f"'{inp}' is not palindrome")