# Author: Hemanth Bathini
# Date: 09/24/2024
# Description: To convert numbers to roman numerals using unicodes
n = int(input("Enter a number between 1 and 9 to convert this to a roman numeral: "))

if n == 1:
    print("your roman number is: \u2160")
elif n == 2:
    print("Your roman number is: \u2161")
elif n == 3:
    print("your roman number is: \u2162")
elif n == 4:
    print("your roman number is: \u2163")
elif n == 5:
    print("your roman number is: \u2164")
elif n == 6:
    print("your roman number is: \u2165")
elif n == 7:
    print("your roman number is: \u2166")
elif n == 8:
    print("your roman number is: \u2167")
elif n == 9:
    print("your roman number is: \u2168")
else:
    print(str(n) + " is outside the allowed range of 1 to 9")
