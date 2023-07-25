class Myint():
    def __init__(self, number):
        self.number = number

    def toRoman(self):
        roman_number = ""
        roman_symbol = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        number_temp = self.number
        for value, symbol in roman_symbol.items():
            while number_temp >= value:
                roman_number += symbol
                number_temp -= value

        return roman_number

    def __add__(self, another):
        res = int((self.number + another.number) * 1.5)
        return Myint(res)


print(" *** class MyInt ***")
num1, num2 = map(int, input("Enter 2 number : ").split())

a = Myint(num1)
b = Myint(num2)

print(str(num1)+" convert to Roman : "+ a.toRoman())
print(str(num2)+" convert to Roman : "+ b.toRoman())
print(f"{num1} + {num2} = {(a+b).number}")
