class Calculator:
    def __init__(self, num):
        self.num = num

    def __add__(self, another):
        return int(self.num + another.num)

    def __sub__(self, another):
        return int(self.num - another.num)

    def __mul__(self, another):
        return int(self.num * another.num)

    def __truediv__(self, another):
        return float(self.num / another.num)

x, y = input("Enter num1 num2 : ").split(",")

x, y = Calculator(int(x)), Calculator(int(y))

print(x + y, x - y, x * y, x / y, sep = "\n")