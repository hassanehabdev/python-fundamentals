
# Lesson 6: If Statements
# Exercises 1–10


# Exercise 1: Check if a number is positive, negative, or zero

x = 0

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")


# Exercise 2: Check if a number is greater than 10

x = 11

if x > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")


# Exercise 3: Check if a number is between 1 and 100

num = 30

if 1 <= num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is not between 1 and 100")


# Exercise 4: Check if a number is less than 50 or greater than 100

num = 70

if num < 50 or num > 100:
    print("Number is less than 50 or greater than 100")
else:
    print("Number is between 50 and 100")


# Exercise 5: Check if a number is a single-digit non-negative number

num = 7

if 0 <= num <= 9:
    print("Number is a single digit")
else:
    print("Number is not a single digit")


# Exercise 6: Check if a number is equal to 10

num = 10

if num == 10:
    print("Number is equal to 10")
elif num > 10:
    print("Number is greater than 10")
else:
    print("Number is less than 10")


# Exercise 7: Check if a number is greater than 0 and less than 100

num = 75

if 0 < num < 100:
    print("Number is greater than zero and less than 100")
else:
    print("Number is not in the specified range")


# Exercise 8: Check if a number is between 50 and 100 inclusive

num = 75

if 50 <= num <= 100:
    print("Number is between 50 and 100 inclusive")
else:
    print("Number is not in the specified range")


# Exercise 9: Check if a number is between 1 and 10 or between 90 and 100

num = 95

if 1 <= num <= 10 or 90 <= num <= 100:
    print("Number is between 1 and 10 or between 90 and 100")
else:
    print("Number is not in the specified range")


# Exercise 10: Check if a number is even or odd

num = 7

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
