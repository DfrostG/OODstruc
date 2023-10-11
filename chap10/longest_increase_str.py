inp = [int(i) for i in input("Data : ").split()]
lis = 1 #lis = longest increasing string
res = [inp[0]]
print(f"1 : {res}")

for i in range(1, len(inp)):
    for j in range(len(res)):
        if inp[i] > res[-1]:
            res.append(inp[i])
            if len(res) > lis:
                lis = len(res)
            break
        else:
            if len(res) == 1:
                res[-1] = inp[i]
            else:
                res.pop(-1)

    print(f"{i + 1} : {res}")
print(f"longest increasing subsequence : {lis}")