
# ============================================================
# Lesson 15: Import Math / Math Module
# ============================================================


# Exercise 1: Convert an integer to a float

a = 2
b = float(a)

print("Value of b (float):", b)


# Exercise 2: Create a complex number

a = 2
b = complex(a, 5)

print("Value of b (complex):", b)


# Exercise 3: Print the absolute value of a negative number

number = int(input("Enter the number: "))

if number < 0:
    print("Absolute value:", abs(number))
else:
    print("Number:", number)


# Exercise 4: Classify a number as negative, positive, or zero

number = int(input("Enter the number: "))

if number < 0:
    print("negative")
elif number > 0:
    print("positive")
else:
    print("zero")


# Exercise 5: Find the maximum of four numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

maximum = max(num1, num2, num3, num4)

print("The maximum number is:", maximum)


# Exercise 6: Find the minimum of four numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

minimum = min(num1, num2, num3, num4)

print("The minimum number is:", minimum)


# Exercise 7: Divide two numbers and round the result to two decimal places

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = round(num1 / num2, 2)

print("Result:", result)


# Exercise 8: Access the value of pi from the math module

import math

pi_value = math.pi

print("The value of Pi:", round(pi_value, 2))


# Exercise 9: Round a number up using ceil()

result = math.ceil(2.1)

print("Rounded up:", result)


# Exercise 10: Round a number down using floor()

result = math.floor(2.1)

print("Rounded down:", result)
