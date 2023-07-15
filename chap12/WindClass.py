print(" *** Wind classification ***")
v = float(input("Enter wind speed (km/h) : "))

if 0 < v and v < 51.99:
    print("Wind classification is Breeze.")
        
elif 52.00 <= v and v < 55.99:
    print("Wind classification is Depression.")
        
elif 56.00 <= v and v < 101.99:
    print("Wind classification is Tropical Storm.")
        
elif 102.00 <= v and v < 208.99:
    print("Wind classification is Typhoon.")
        
elif 209 <= v:
    print("Wind classification is Super Typhoon.")
        
elif v < 0:
    print("!!!Wrong value can't classify.")