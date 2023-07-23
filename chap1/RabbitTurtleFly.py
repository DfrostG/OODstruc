print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = input("Enter Input : ").split(" ")
t = int(d) / (int(Vt) - int(Vr))
x = int(Vf) * t
print(f"{x:.2f}")