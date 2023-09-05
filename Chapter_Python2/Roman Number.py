#จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่
# M=1000    CM=900    D=500    CD=400,
# C=100    XC=90    L=50    XL=40,
# X=10    IX=9    V=5    IV=4    I=1
# เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I
# (https://roman-numerals.info/)

class translator:
    def deciToRoman(self, num):
        if not 0 < num < 4000:
            return "Invalid input"
        roman_number = {
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

        roman_num = ""
        for value, symbol in roman_number.items():
            while num >= value:
                roman_num += symbol
                num -= value
        return roman_num

    def romanToDeci(self, s):
        roman_numerals = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        decimal_num = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in roman_numerals:
                decimal_num += roman_numerals[s[i:i+2]]
                i += 2
            else:
                decimal_num += roman_numerals[s[i]]
                i += 1
        return decimal_num


num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))
