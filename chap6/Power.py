def power(base, top, ans = 1):
    if top > 0:
        ans = ans * base
        power(base, top -1, ans)
    if top == 0:
        print(ans)

inp = input("Enter Input a b : ").split(",")
power(int(inp[0]),int(inp[1]))