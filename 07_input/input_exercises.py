# Lesson 9: Input
# Exercises 1–10


# Exercise 1: Get the user's name and greet them

name = input("Enter your name: ")
print("Hello,", name)


# Exercise 2: Get the user's age and display it

age = input("Enter your age: ")
print("Your age is:", age)


# Exercise 3: Calculate the sum of two numbers entered by the user

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

total = first_number + second_number

print("The sum is:", total)


# Exercise 4: Get the user's favorite color and display it

favorite_color = input("Enter your favorite color: ")
print("Your favorite color is:", favorite_color)


# Exercise 5: Get the user's city and display a message

city = input("Enter your city: ")
print("You live in", city)


# Exercise 6: Get the user's birth year and calculate their age

birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year

print("Your age is:", age)


# Exercise 7: Get the user's email address and display it

email = input("Enter your email address: ")
print("Your email address is:", email)


# Exercise 8: Get the user's age and display an age category

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# Exercise 9: Get the user's favorite fruit and print it three times

favorite_fruit = input("Enter your favorite fruit: ")

for i in range(3):
    print(favorite_fruit)


# Exercise 10: Get the user's first name and print each character separately

first_name = input("Enter your first name: ")

print("Characters in your name:")

for char in first_name:
    print(char)
