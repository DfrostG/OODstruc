class MyInt:
    def __init__(self, num):
        self.num = num
        self.num_to_roman = {
            "M" : 1000,
            "CM" : 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "I" : 1
        }

    def toRoman(self):
        valTemp = self.num
        romanNum = ""
        while valTemp > 0:
            for key, val in self.num_to_roman.items():
                if val <= valTemp:
                    romanNum += key
                    valTemp -= val
                    break
        return romanNum
    
    def __add__(self, other):
        return MyInt(int((self.num + other.num)*1.5))
    
print(" *** class MyInt ***")
n1, n2 = [int(x) for x in input("Enter 2 number : ").split()]
a = MyInt(n1)
b = MyInt(n2)
print(f"{a.num} convert to Roman : {a.toRoman()}")
print(f"{b.num} convert to Roman : {b.toRoman()}")
print(f"{a.num} + {b.num} = {(a+b).num}")