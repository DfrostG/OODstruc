def bi_search(l, r, x):
    if x == 1:
        center = 1
    else:
        center = (r + l) // 2
        
    if center * center == x:
        return center
    elif center * center < x:
        if (center + 1) ** 2 > x:
            return center
        return bi_search(center,r,x)
    elif center * center > x:
        if (center - 1) ** 2 < x:
            return center - 1
        return bi_search(l, center, x)
    

inp = int(input("simple sqrt: "))
print(bi_search(0, inp, inp))